class Cart:
    def __init__(self, request):
        self.request = request.user

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart
