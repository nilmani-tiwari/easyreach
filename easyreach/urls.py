"""easyreach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from common.views import *
from texteditor.views import *
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', home,name="home"),
    path('index.html', home2,name="home2"),
    path('show_ads/<id>/', show_ads, name='show_ads'),
    path('login_user/', login_user,name="login_user"),
    path('signup/', signup,name="signup"),
    path('signout/', logoutUser,name="logout"),
    path('base/', base,name="base"),
    path('submit-form/', form_submit,name="form_submit"),
    path('key-press/', press_key,name="press_key"),





    path('forgot_password/', forgot_password,name="forgot_password"),
    path('text2html/', TextHtml,name="text_html"),
    path('sitemaps/main.xml', MainSitemap.as_view(), name='main_sitemap'),

    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name="signout"),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



