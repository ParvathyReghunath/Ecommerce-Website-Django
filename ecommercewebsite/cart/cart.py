class Cart():
    def __init__ (self,request):

        self.session = request.session

        # to get the current session key

        cart=self.session.get('session_key')
        
        # assign a new session key
        
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        # to access it in all pages
        self.cart=cart
