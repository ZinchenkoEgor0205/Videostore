from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app_basket.basket import Basket
from app_basket.models import Order
from app_basket.forms import BasketAddVideocardForm, OrderForm
from app_main.models import Videocard


@require_POST
def basket_add_view(request, videocard_id):
    basket = Basket(request)
    videocard= get_object_or_404(Videocard, id=videocard_id)
    form = BasketAddVideocardForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(videocard=videocard, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('basket_detail_view')

def basket_remove_view(request, videocard_id):
    basket = Basket(request)
    videocard = get_object_or_404(Videocard, id=videocard_id)
    basket.remove(videocard)
    return redirect('basket_detail_view')

@login_required
def basket_detail_view(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = BasketAddVideocardForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'basket_detail.html')

@login_required
def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(request.user.id)
            Order.objects.create(
                name_surname=cd['name_surname'],
                phone=cd['phone'],
                email=cd['email'],
                city=cd['city'],
                street=cd['street'],
                house=cd['house'],
                housing=cd['housing'],
                apartment=cd['apartment'],
                user_id=request.user.id,
            )
            basket = Basket(request)
            basket.clear()
            return redirect('gratitude_view')
    else:
        form = OrderForm()
    return render(request, 'order.html', context={'form': form})

def gratitude_view(request):
    return render(request, 'gratitude.html')