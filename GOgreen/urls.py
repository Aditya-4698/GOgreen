from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='home'),
    path('events/', views.events, name='events'),
    path('service/', views.service, name='service'),
    path('gallery/', views.gallery, name='gallery'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('donation/', views.donation, name='donation'),
    path('contact/', views.contact, name='contact'),
    path('causes/', views.causes, name='causes'),
    path('about/', views.about, name='about'),
    path('404/', views.four_oh_four, name='error_404'),
    path('blog/', views.blog, name='blog'),
    path('base/', views.base, name='base'),
]
