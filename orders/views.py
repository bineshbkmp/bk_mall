from django.shortcuts import redirect, render
from django.contrib.auth import aauthenticate
from . models import Order,OrderedItem
from products.models import Product
# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('account')
        else :
            user=request.user
            customer=user.customer_profile
            quantity=int(request.POST.get('quantity'))
            product_id=request.POST.get('product_id')
            cart_obj,created=Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            product=Product.objects.get(pk=product_id)
            ordered_item,created=OrderedItem.objects.get_or_create(
                product=product,
                owner=cart_obj,
              
            )
            if created:
                ordered_item.quantity=quantity
                ordered_item.save()
            else:
                ordered_item.quantity+=quantity
                ordered_item.save()
            return redirect('cart')

        