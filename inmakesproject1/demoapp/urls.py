
from .import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),

#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('home/',views.home,name='home'),
#     path('thankyou/',views.thankyou,name='thankyou')
]
