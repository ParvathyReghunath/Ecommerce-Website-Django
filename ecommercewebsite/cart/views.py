from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prod()
    return render(request,'cart_summary.html',{'cart_products':cart_products})

def cart_add(request):
    cart = Cart(request)
    # print("cart_add view called")
    
    if request.POST.get('action') == 'post':
        # print("post action is post")
        # print(request.POST)
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'error': 'Product ID is missing'}, status=400)
        product=get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_quantity=cart.__len__()
        response=JsonResponse({'qty' : cart_quantity})
        response=JsonResponse({'Product Name' : product.name})
        return response

  

# def cart_add(request):
#     cart = Cart(request)

#     if request.POST.get('action') == 'post':
#         # Retrieve product ID from POST data
#         product_id = request.POST.get('product_id')
#         if not product_id:
#             return JsonResponse({'error': 'Product ID is missing'}, status=400)

#         try:
#             # Fetch the product from the database
#             product = get_object_or_404(Product, id=product_id)
#             cart.add(product=product)

#             # Respond with success
#             return JsonResponse({'Product Name': product.name})

#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found'}, status=404)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return JsonResponse({'error': 'Invalid action'}, status=400)

    
def cart_update(request):
    pass

def cart_delete(request):
    pass







