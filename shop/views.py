from itertools import product

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from shop.models import Shop, Category, Product
from .models import Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignupForm, UpdateUserForm , UpdatePasswordForm

# from .serializers import ProductSerializer

#This is only a test for user want to conver or create Webapplication
#@api_view(['GET' , 'POST'])
#def index(request):
    #print(request.data)
    #bag = Product.objects.filter(category_id=1)
    #serializer = ProductSerializer(bag)
    #return Response(dict(request.data))
    #print(serializer)
    #print(serializer.data)
    #return Response(serializer.data)


def listing(request):
    all_categories = Category.objects.all()
    products = Product.objects.all()[:4]
    context = {
        "categories":all_categories,
        "products":products,
    }
    return render(request, 'shop/index.html', context=context)


def about(request):
    return render(request, 'shop/about.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect("listing")
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('listing')
        else:
            messages.success(request, 'We Have Problem To Login Your Account')
            return redirect('login')
    else:
        return render(request, 'shop/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('listing')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('listing')
        else:
            messages.success(request, 'Please correct the error below.')
            return redirect('signup')
    else:
        return render(request, 'shop/signup.html', {'form': form})


def bagtest2(request):
    bag = Product.objects.filter(category_id=1)
    bag.count()
    context = {'bag': bag}
    return render(request, 'bag.html', context)


def sneakers(request):
    sneakers = Product.objects.filter(category_id=2)
    sneakers.count()
    context = {'sneakers': sneakers}
    return render(request, 'sneaker.html', {'sneakers': sneakers})


def pant(request):
   pants = Product.objects.filter(category_id=3)
   pants.count()
   context = {'pants': pants}
   return render(request, 'pant.html', {'pants': pants})


def tshirt(request):
    tshirt = Product.objects.filter(category_id=4)
    tshirt.count()
    context = {'tshirt': tshirt}
    return render(request, 'tshirt.html', {'tshirt': tshirt})


def watch(request):
    watch = Product.objects.filter(category_id=5)
    watch.count()
    context = {'watch': watch}
    return render(request, 'watch.html', {'watch': watch})


def sock(request):
    sock = Product.objects.filter(category_id=6)
    sock.count()
    context = {'sock': sock}
    return render(request, 'sock.html', {'sock': sock})


def odclon(request):
    odclon = Product.objects.filter(category_id=7)
    odclon.count()
    context = {'odclon': odclon}
    return render(request, 'odclon.html', {'odclon': odclon})


def jacket(request):
    jacket = Product.objects.filter(category_id=8)
    jacket.count()
    context = {'jacket': jacket}
    return render(request, 'jacket.html', {'jacket': jacket})


def Detailbag(request, pk):
   detailbag = Product.objects.filter(id=pk, category_id=1)
   detailbag.count()

   last_quantity = request.session.get('last_quantity', 1)
   last_size = request.session.get('last_size', 'm')

   

   print("Last quantity from session:", last_quantity)

   context = {
       'detailbag': detailbag,
       "last_quantity" : last_quantity,
       "last_size": last_size,
    }

   return render(request, 'Detailbag.html', context)


def Detailsneaker(request, pk):
    detailsneaker = Product.objects.filter(id=pk, category_id=2)
    detailsneaker.count()
    context = {'detailsneaker': detailsneaker}
    return render(request, 'Detailsneaker.html', context)


def Detailpant(request, pk):
  detailpant = Product.objects.filter(id=pk, category_id=3)
  detailpant.count()
  context = {'detailpant': detailpant}
  return render(request, 'Detailpant.html', context)



def Detailtshirt(request, pk):
    detailtshirt = Product.objects.filter(id=pk, category_id=4)
    detailtshirt.count()
    context = {'detailtshirt': detailtshirt}
    return render(request , 'Detailtshirt.html', context)


def Detailwatch(request, pk):
    detailwatch = Product.objects.filter(id=pk, category_id=5)
    detailwatch.count()
    context = {'detailwatch': detailwatch}
    return render(request, 'Detailwatch.html', context)


def Detailsock(request, pk):
    detailsock = Product.objects.filter(id=pk, category_id=6)
    detailsock.count()
    context = {'detailsock': detailsock}
    return render(request, 'Detailsock.html', context)


def Detailodclon(request, pk):
    detailodclon = Product.objects.filter(id=pk, category_id=7)
    detailodclon.count()
    context = {'detailodclon': detailodclon}
    return render(request, 'Detailodclon.html', context)


def Detailjacket(request, pk):
    detailjacket = Product.objects.filter(id=pk, category_id=8)
    detailjacket.count()
    context = {'detailjacket': detailjacket}
    return render(request, 'Detailjacket.html', context)


def update_user(request):
    if User.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)


        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            return redirect('listing')
        messages.success(request, 'Your Account Has Been Updated')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'You are not logged in yet')
        return redirect('listing')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

    if request.method == 'POST':

     pass

    else:
        form = UpdatePasswordForm(request.POST)
        return render(request, 'update_password.html', {'form': form})

    return redirect('listing')
