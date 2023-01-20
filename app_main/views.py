from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from app_basket.forms import BasketAddVideocardForm
from app_main.models import Videocard
from django.views.generic.detail import DetailView

def main_view(request):
    videocards = Videocard.objects.filter(promo_type='r')
    videocards_promo = Videocard.objects.filter(promo_type='n')
    user = request.user
    return render(request, 'main.html', context= {'videocards': videocards, 'videocards_promo': videocards_promo, 'user': user})

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

