from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app_basket.basket import Basket
from app_basket.models import Order
from app_basket.forms import BasketAddVideocardForm, OrderForm
from app_main.models import Videocard
from app_user.models import Discount


@require_POST
@login_required(login_url='/user/login/')
def basket_add_view(request, videocard_id):
    basket = Basket(request)
    videocard = get_object_or_404(Videocard, id=videocard_id)
    form = BasketAddVideocardForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(videocard=videocard, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('basket_detail_view')


@login_required(login_url='/user/login/')
def basket_remove_view(request, videocard_id):
    basket = Basket(request)
    videocard = get_object_or_404(Videocard, id=videocard_id)
    basket.remove(videocard)
    return redirect('basket_detail_view')


@login_required(login_url='/user/login/')
def basket_detail_view(request):
    basket = Basket(request)
    for item in basket:
        item['price'] = Decimal(item['price']) * request.user.profile.discount.price_multiplier
        item['update_quantity_form'] = BasketAddVideocardForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'basket_detail.html')


@login_required(login_url='/user/login/')
def order_view(request):
    basket = Basket(request)
    total_sum = sum(
        [int(i['price']) * int(i['quantity']) for i in basket])
    total_sum_with_discount = sum(
        [int(i['price']) * int(i['quantity']) for i in basket]) * request.user.profile.discount.price_multiplier
    user = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
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
            user.profile.total_sum += total_sum
            user.profile.save()

            total_user_sum = user.profile.total_sum
            discount_status = Discount.objects.all().filter(required_sum__lte=total_user_sum).order_by(
                'required_sum').last()
            if user.profile.discount != discount_status:
                user.profile.discount = discount_status
                user.profile.save()
            basket.clear()
            return redirect('gratitude_view')
    else:
        form = OrderForm()
        discount = total_sum - total_sum_with_discount
    return render(request, 'order.html', context={'form': form, 'user': user, 'total_sum_with_discount': total_sum_with_discount, 'discount': discount})


def gratitude_view(request):
    return render(request, 'gratitude.html')
