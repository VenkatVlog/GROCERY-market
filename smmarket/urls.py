from django.urls import path
from .middlewares.auth import  auth_middleware
from django.contrib.auth.decorators import login_required
from .views import HomeView,Shop,Signup,Login,OrderView,logout,CheckOut,Cart

urlpatterns = [
    path('shop/', Shop.as_view(),name='shop'),
    path('products/', auth_middleware(Cart.as_view()),name='cart'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
