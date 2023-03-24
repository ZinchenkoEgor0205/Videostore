from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_basket.forms import BasketAddVideocardForm
from app_main.forms import FilterForm
from app_main.models import Videocard
from django.views.generic.detail import DetailView
from videostore_project import settings


def main_view(request):
    videocards = Videocard.objects.filter(promo_type='r')
    videocards_promo = Videocard.objects.filter(promo_type='n')
    user = request.user
    return render(request, 'main.html', context= {'videocards': videocards, 'videocards_promo': videocards_promo, 'user': user})


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