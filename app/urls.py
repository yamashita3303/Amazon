from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

    path('', views.item, name='item'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('cart/<int:item_id>/', views.cart, name='cart'),
    path('history', views.history, name='history'),
    path('payment', views.payment, name='payment'),
    path('address', views.address, name='address'),
    path('end', views.end, name='end'),
]