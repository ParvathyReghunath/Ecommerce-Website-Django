from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prod()
    quantities=cart.get_quants()
    return render(request,'cart_summary.html',{'cart_products':cart_products,'quantities':quantities})

def cart_add(request):
    cart = Cart(request)
    # print("cart_add view called")
    
    if request.POST.get('action') == 'post':
        # print("post action is post")
        # print(request.POST)
        product_id = request.POST.get('product_id')
        product_qty=request.POST.get('product_qty')
        if not product_id:
            return JsonResponse({'error': 'Product ID is missing'}, status=400)
        product=get_object_or_404(Product, id=product_id)
        cart.add(product=product,quantity=product_qty)
        cart_quantity=cart.__len__()
        response=JsonResponse({'qty' : cart_quantity})
        response=JsonResponse({'Product Name' : product.name})
        return response



    
def cart_update(request):
    cart = Cart(request)        
    if request.POST.get('action') == 'post':
        # print("entered update")
        product_id = request.POST.get('product_id')
        product_qty=request.POST.get('product_qty')
        
        cart.update(product=product_id, quantity=product_qty)
        response=JsonResponse({'qty' : product_qty})
        return response


def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        product_id=request.POST.get('product_id')
        cart.delete(product=product_id)
        response=JsonResponse({'id' : product_id})
        return response
        







