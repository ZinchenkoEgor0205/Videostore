import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from app_basket.forms import BasketAddVideocardForm
from app_main.forms import FilterForm
from django.views.generic.detail import DetailView
from videostore_project import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class MainView(View):

    def get_random_videocard_promo(self):
        videocard_max_id = Videocard.objects.filter(promo_type='n').aggregate(max_id=Max("id"))
        max_id = videocard_max_id['max_id']
        while True:
            pk = random.randint(1, max_id)
            videocard_promo = Videocard.objects.filter(promo_type='n', pk=pk).first()
            if videocard_promo:
                return videocard_promo
    def get(self, request):
        videocards = Videocard.objects.all()
        videocards_promo = self.get_random_videocard_promo()
        user = request.user
        return render(request, 'main.html',
                      context={'videocards': videocards, 'videocards_promo': videocards_promo, 'user': user})

# def main_view(request):
#     videocards = Videocard.objects.all()
#     videocards_promo = Videocard.objects.filter(promo_type='n')
#     user = request.user
#     return render(request, 'main.html', context={'videocards': videocards, 'videocards_promo': videocards_promo, 'user': user})


def videocards_sorted_view(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            parameter = form.cleaned_data['parameter']
            search = form.cleaned_data['search']
            if search:
                videocards = Videocard.objects.filter(name__contains=search)
            else:
                videocards = Videocard.objects.all()
            if parameter == 1:
                videocards = videocards.order_by('price')
            else:
                videocards = videocards.order_by('price').reverse()
            form = FilterForm()
            context = {
                'videocards': videocards,
                'form': form
            }
            return render(request, 'videocards_sorted.html', context=context)
    else:
        form = FilterForm()
    videocards = Videocard.objects.all()
    context = {
        'videocards': videocards,
        'form': form,
    }
    return render(request, 'videocards_sorted.html', context=context)



class VideocardDetailView(DetailView):
    model = Videocard
    template_name = 'videocard_detail.html'
    context_object_name = 'videocard'
    basket_videocard_form = BasketAddVideocardForm()
    extra_context = {'basket_videocard_form': basket_videocard_form}

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        obj = Videocard.objects.get(id=pk)
        return obj


def set_language(request):
    lang = request.GET.get('l', 'en')
    request.session[settings.LANGUAGE_SESSION_KEY] = lang
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


class VideocardCreateView(PermissionRequiredMixin, CreateView):
    model = Videocard
    fields = ['name', 'image', 'manufacturer', 'vendor', 'image_big', 'info', 'price']
    template_name = 'videocard_create.html'
    success_url = reverse_lazy('main_view')
    permission_required = 'add_videocard'


class VideocardUpdateView(PermissionRequiredMixin, UpdateView):
    model = Videocard
    fields = ['name', 'image', 'manufacturer', 'vendor', 'image_big', 'info', 'price']
    template_name = 'videocard_update.html'
    permission_required = 'edit_videocard'

    def get_success_url(self):
        return reverse('videocard_detail', kwargs={'pk': self.object.pk})

class VideocardInfoCreateView(PermissionRequiredMixin, CreateView):
    model = VideocardInfo
    fields = '__all__'
    template_name = 'videocard_info_create.html'
    success_url = reverse_lazy('main_view')
    permission_required = 'add_videocardinfo'

class VideocardInfoUpdateView(PermissionRequiredMixin, UpdateView):
    model = VideocardInfo
    fields = '__all__'
    template_name = 'videocard_info_update.html'
    success_url = reverse_lazy('main_view')
    permission_required = 'edit_videocardinfo'



class VideocardSerializedListView(APIView):
    """Список всех видеокарт магазина"""

    def get(self, request):
        videocards = Videocard.objects.all()
        serializer = VideocardListSerializer(videocards, many=True)
        return Response(serializer.data)


class VideocardSerializedDetailView(APIView):

    def get(self, request, pk):
        videocard = Videocard.objects.get(id=pk)
        serializer = VideocardDetailSerializer(videocard)
        return Response(serializer.data)
