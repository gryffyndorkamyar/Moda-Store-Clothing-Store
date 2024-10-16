"""
URL configuration for myproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from shop import views
from shop.views import listing
from shop import views
from shop.views import listing
#from shop.views import index
from shop.views import login_user, logout_user, signup, update_user, update_password
from shop.views import bagtest2, sneakers, pant, tshirt, watch, sock, odclon, jacket
#from shop.views import Detailbag, Detailsneaker, Detailpant, Detailtshirt,Detailwatch, Detailsock, Detailodclon,Detailjacket ,


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listing, name="listing"),
    #path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name="login"),
    path('update_user/', views.update_user, name="update_user"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('update_password',views.update_password , name="update_password"),
    path('bag/', views.bagtest2, name="bag"),
    path('detailbag/<int:pk>', views.Detailbag , name="detailbag"),
    path('sneaker/', views.sneakers, name="sneaker"),
    path('detailsneaker/<int:pk>', views.Detailsneaker , name="detailsneaker"),
    path('pant/', views.pant, name='pant'),
    path('detailpant/<int:pk>', views.Detailpant, name="detailpant"),
    path('tshirt/', views.tshirt, name="tshirt"),
    path('detailtshirt/<int:pk>', views.Detailtshirt, name="detailtshirt"),
    path('watch/', views.watch, name="watch"),
    path('detailwatch/<int:pk>', views.Detailwatch, name="detailwatch"),
    path('sock/', views.sock, name="sock"),
    path('detailsock/<int:pk>', views.Detailsock, name="detailsock"),
    path('odclon/', views.odclon, name="odclon"),
    path('detailodclon/<int:pk>', views.Detailodclon, name="detailodclon"),
    path('jacket/', views.jacket, name="jacket"),
    path('detailjacket/<int:pk>', views.Detailjacket, name="detailjacket"),
    path("cart/", include("cart.urls")),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
