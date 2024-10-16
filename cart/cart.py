from shop.models import Product
from decimal import Decimal

CART_SESSION_ID = 'cart'
class Cart:
    def __init__(self,request):
        self.session = request.session 
        cart = self.session.get(CART_SESSION_ID)

        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        
        self.cart = cart
    
    
    def add(self,product,quantity=1,size=None, override_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price':str(product.price),
                'size': size
            }
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.cart[product_id]['size'] = size
        self.save()
    
    def save(self):
        self.session.modified = True

    def remove(self,product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():

            # item['price'] = int(item['price'])
            item['total_price'] = item['product'].price * item['quantity']
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    

    def get_total_price(self):
        return sum(item['quantity'] * item['product'].price for item in self.cart.values())
    
    def clear(self):
        
        del self.session[CART_SESSION_ID]
        self.save()

