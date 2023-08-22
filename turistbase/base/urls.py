from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about-us'),
    # path('', views.booking_view, name='booking')
]
