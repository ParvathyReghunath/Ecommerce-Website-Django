from store.models import Product


class Cart():
    def __init__ (self,request):

        self.session = request.session

        # to get the current session key

        cart=self.session.get('session_key')
        
        # assign a new session key
        
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        # to access it in all page
        self.cart=cart


    def add(self,product,quantity):
        product_id=str(product.id)
        product_qty=str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id]={'price':str(product.price)}
            self.cart[product_id]=int(product_qty)
        self.session.modified= True 


    def __len__(self):
        return len(self.cart)
    
    def get_prod(self):
        product_id=self.cart.keys()
        products=Product.objects.filter(id__in=product_id)
        return products
    
    def get_quants(self):
        quantities=self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id=str(product)
        product_qty=int(quantity)
        outcart=self.cart
        outcart[product_id]=product_qty
        self.session.modified =True
        thing = self.cart
        return thing

