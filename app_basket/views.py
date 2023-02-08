from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app_basket.basket import Basket
from app_basket.forms import BasketAddVideocardForm
from app_main.models import Videocard


@require_POST
def basket_add_view(request, videocard_id):
    basket = Basket(request)
    videocard= get_object_or_404(Videocard, id=videocard_id)
    form = BasketAddVideocardForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(videocard=videocard, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('basket_detail')

def basket_remove_view(request, videocard_id):
    basket = Basket(request)
    videocard = get_object_or_404(Videocard, id=videocard_id)
    basket.remove(videocard)
    return redirect('basket_detail')

def basket_detail_view(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = BasketAddVideocardForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'basket_detail.html')
