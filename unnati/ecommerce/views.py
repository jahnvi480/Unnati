from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Product , Cart ,CartQty , Address
from django.contrib.auth.models import User , auth
from django.core.mail import send_mail

# Create your views here.
def index(request):
    products = Product.objects.all()
    carts = Cart.objects.all()
    cartid = request.POST.get('user')
    add = Address.objects.filter(users=cartid)
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin_code = request.POST.get('zip')
        add.update(address=address, city=city, state=state, pin_code=pin_code, phone=phone)
        send_mail('Congratulations!! Order placed',
                  'Thank you for shopping with UNNATI. Your Order will be delivered in 10 days of order placed.',
                  '', [email], fail_silently=False)
        return redirect('/unnati')
    params = {'product': products, 'cart': carts}
    return render(request, 'shop/index.html', params)

def cart(request):
    items = None
    product_id = request.POST.get('product')
    product = Product.objects.filter(id=product_id)
    cartid = request.POST.get('user')
    cart = Cart.objects.all()
    carts = Cart.objects.filter(users=cartid)
    cartsqty = CartQty.objects.filter(users=cartid)
    if product_id == '1':
        lemonade = request.POST.get('qty')
        cartsqty.update(Lemonade=lemonade)
    elif product_id == '2':
        pc = request.POST.get('qty')
        cartsqty.update(P_C=pc)
    elif product_id == '3':
        achar = request.POST.get('qty')
        cartsqty.update(Aachar=achar)
    elif product_id == '4':
        papad = request.POST.get('qty')
        cartsqty.update(Papad=papad)
    elif product_id == '5':
        kmg = request.POST.get('qty')
        cartsqty.update(K_M_G=kmg)
    for prod in carts:
        items = prod.products.all()
        prod.products.add(product.first())
        for x in cartsqty:
            total = x.Aachar * 150 + x.Papad * 60 + x.Lemonade * 25 + x.P_C * 50 + x.K_M_G * 10
            carts.update(total=total)
    params = {'cartitem': items, 'qty': cartsqty[0], 'carts': carts[0], 'cart': cart}
    return render(request, 'shop/cart.html', params)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        user1 = request.POST['username']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('/unnati/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('/unnati/register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                password=password1, username=username)
                user.save()
                cart = Cart.objects.create(users=user1)
                cart.save()
                cartqty = CartQty.objects.create(users=user1)
                cartqty.save()
                add = Address.objects.create(users=user1)
                add.save()
                return redirect('/unnati/login')
        else:
            messages.info(request, 'password not matching')
            return redirect('/unnati/register')
        return redirect('/unnati')
    else:
        return render(request, 'shop/reg.html')

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/unnati')
        else:
            messages.info(request, 'not registered')
            return redirect('/unnati/login')
    else:
        return render(request, 'shop/login.html')

def account_logout(request):
    auth.logout(request)
    return redirect('/unnati')

def product(request,myid):
    carts = Cart.objects.all()
    products = Product.objects.filter(id=myid)
    return render(request, 'shop/pro.html', {'product': products[0], 'cart': carts})

def checkout(request):
    cartid = request.POST.get('user')
    items = None
    c = Cart.objects.all()
    carts = Cart.objects.filter(users=cartid)
    cartsqty = CartQty.objects.filter(users=cartid)
    for prod in carts:
        items = prod.products.all()
    params = {'cartitem': items, 'qty': cartsqty[0], 'carts': carts[0], 'cart': c}
    return render(request, 'shop/checkout.html', params)


