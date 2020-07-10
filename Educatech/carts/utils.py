from .models import Cart

def get_or_create_cart(request):

    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()
    #Creado una session
    #request.session['cart_id'] = '123'
    #almacenando valor obtenido por el request
    #valor = request.session.get('cart_id')
    #Eliminar session
    #request.session['cart_id'] = None
    if cart is None:
        cart = Cart.objects.create(user=user)
    
    if user and cart.user is None:
        cart.user = user
        cart.save()
    
    request.session['cart_id'] = cart.cart_id
    return cart
