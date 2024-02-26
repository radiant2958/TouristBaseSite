from django.urls import path
from . import views
from base.tests import error400
urlpatterns = [
    path('', views.title_base, name='title_base'),
    path('about-us', views.about, name='about-us'),
    path('success/', views.success_page, name='success_page'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.new, name='new'),
    path('room/', views.room, name='room'),
    path('room0/', views.roomZero, name='roomZero'),
    path('room1/', views.roomOne, name='roomOne'),
    path('room2/', views.roomSecond, name='roomSecond'),
    path('room3/', views.roomThird, name="roomThird"),
    path('room4/', views.roomFourth, name="roomFourth"),
    path('room5/', views.roomsTriple, name="roomsTriple"),
    path('handler400/',views.handler400, name='handler400'),
    path('handler500/', views.handler500, name='handler500'),
    path('validate_user_phone/', error400.validate_user_phone, name='error400')
    

]
