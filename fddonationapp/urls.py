from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('userregister', views.userregister.as_view(), name='userregister'),
    path('userregister2', views.userregister2.as_view(), name='userregister2'),
    path('LoginAPIView1', views.LoginAPIView1.as_view(), name='LoginAPIView1'),
    path('UserView', views.UserView.as_view(), name='UserView'),
    path('receiverView', views.receiverView.as_view(), name='receiverView'),
    path('addfood', views.addfood.as_view(), name='addfood'),
    path('allfoodview', views.allfoodview.as_view(), name='allfoodview'),
    path('singlefoodview/<int:id>', views.singlefoodview.as_view(), name='singlefoodview'),
    path('deletesinglefoodview/<int:id>', views.deletesinglefoodview.as_view(), name='deletesinglefoodview'),
    path('updatefood/<int:id>', views.updatefood.as_view(), name='updatefood'),
    path('donarfoodview/<int:id>', views.donarfoodview.as_view(), name='donarfoodview'),
    path('searchfood', views.searchfood.as_view(), name='searchfood'),
    path('receiverfoodview', views.receiverfoodview.as_view(), name='receiverfoodview'),
    path('acceptingAPIView', views.AcceptingAPIView.as_view(), name='acceptingAPIView'),
    path('receiveracceptingview', views.receiveracceptingview.as_view(), name='receiveracceptingview'),
    path('deletereceiveracceptingview/<int:id>', views.deletereceiveracceptingview.as_view(), name='deletereceiveracceptingview'),
    path('donaracceptingview/<int:id>', views.donaracceptingview.as_view(), name='donaracceptingview'),
    path('donarApprove_orderAPIView/<int:id>', views.donarApprove_orderAPIView.as_view(), name='donarApprove_orderAPIView'),
    path('donationapproved/<int:id>', views.donationapproved.as_view(), name='donationapproved'),
    path('donationpending/<int:id>', views.donationpending.as_view(), name='donationpending'),
    



]