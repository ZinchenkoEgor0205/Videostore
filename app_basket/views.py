from datetime import timedelta
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.decorators.http import require_POST

from app_basket.basket import Basket
from app_basket.models import Order, OrderVideocard
from app_basket.forms import BasketAddVideocardForm, OrderForm
from app_main.models import Videocard
from app_user.models import Discount


class BasketDetailView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')

    def get(self, request):
        basket = Basket(request)
        for item in basket:
            item['price'] = Decimal(item['price']) * request.user.profile.discount.price_multiplier
            item['update_quantity_form'] = BasketAddVideocardForm(
                initial={'quantity': item['quantity'], 'update': True})
        return render(request, 'basket_detail.html')



class BasketAddView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')

    def post(self, request, videocard_id):
        basket = Basket(request)
        videocard = get_object_or_404(Videocard, id=videocard_id)
        form = BasketAddVideocardForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            basket.add(videocard=videocard, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('basket_detail_view')


class BasketRemoveView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')

    def get(self, request, videocard_id):
        basket = Basket(request)
        videocard = get_object_or_404(Videocard, id=videocard_id)
        basket.remove(videocard)
        return redirect('basket_detail_view')


class OrderView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')

    def get(self, request):
        basket = Basket(request)
        total_sum = sum(
            [int(i['price']) * int(i['quantity']) for i in basket])
        total_sum_with_discount = total_sum * request.user.profile.discount.price_multiplier
        user = request.user
        form = OrderForm()
        discount = total_sum - total_sum_with_discount

        return render(request, 'order.html',
                      context={'form': form, 'user': user, 'total_sum_with_discount': total_sum_with_discount,
                               'discount': discount})

    def post(self, request):
        basket = Basket(request)
        total_sum = sum(
            [int(i['price']) * int(i['quantity']) for i in basket])
        total_sum_with_discount = total_sum * request.user.profile.discount.price_multiplier
        user = request.user

        discount_expiry = timezone.now() - timedelta(days=365)
        order_history = Order.objects.filter(user=user, date__gte=discount_expiry)
        active_sum = sum([item.sum for item in order_history])
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(
                name_surname=cd['name_surname'],
                phone=cd['phone'],
                email=cd['email'],
                city=cd['city'],
                street=cd['street'],
                house=cd['house'],
                housing=cd['housing'],
                apartment=cd['apartment'],
                sum=total_sum_with_discount,
                user_id=request.user.id,
            )
            for item in basket:
                OrderVideocard.objects.create(
                    videocard=item['videocard'],
                    order=order,
                    quantity=item['quantity'],
                )
            user.profile.total_sum = active_sum
            user.profile.save()

            discount_status = Discount.objects.all().filter(required_sum__lte=active_sum).order_by(
                'required_sum').last()
            if user.profile.discount != discount_status:
                user.profile.discount = discount_status
                user.profile.save()
            basket.clear()
            return redirect('gratitude_view')



# @login_required(login_url=reverse_lazy('login'))
# def order_view(request):
#     basket = Basket(request)
#     total_sum = sum(
#         [int(i['price']) * int(i['quantity']) for i in basket])
#     total_sum_with_discount = total_sum * request.user.profile.discount.price_multiplier
#     user = request.user
#
#     discount_expiry = timezone.now() - timedelta(days=365)
#     order_history = Order.objects.filter(user=user, date__gte=discount_expiry)
#     active_sum = sum([item.sum for item in order_history])
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             order = Order.objects.create(
#                 name_surname=cd['name_surname'],
#                 phone=cd['phone'],
#                 email=cd['email'],
#                 city=cd['city'],
#                 street=cd['street'],
#                 house=cd['house'],
#                 housing=cd['housing'],
#                 apartment=cd['apartment'],
#                 sum=total_sum_with_discount,
#                 user_id=request.user.id,
#             )
#             for item in basket:
#                 OrderVideocard.objects.create(
#                     videocard=item['videocard'],
#                     order=order,
#                     quantity=item['quantity'],
#                 )
#             user.profile.total_sum = active_sum
#             user.profile.save()
#
#             discount_status = Discount.objects.all().filter(required_sum__lte=active_sum).order_by(
#                 'required_sum').last()
#             if user.profile.discount != discount_status:
#                 user.profile.discount = discount_status
#                 user.profile.save()
#             basket.clear()
#             return redirect('gratitude_view')
#     else:
#         form = OrderForm()
#         discount = total_sum - total_sum_with_discount
#     return render(request, 'order.html',
#                   context={'form': form, 'user': user, 'total_sum_with_discount': total_sum_with_discount,
#                            'discount': discount})


def gratitude_view(request):
    return render(request, 'gratitude.html')
