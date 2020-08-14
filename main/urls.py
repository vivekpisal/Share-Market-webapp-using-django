from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('pan',views.pan,name="pan"),
    path('photo',views.photo,name="photo"),
    path('aadhar',views.aadhar,name="aadhar"),
    path('bankst',views.bankst,name="bankst"),
  	path('register',views.register,name="register"),
  	path('panvali/<int:card>/<str:name>/<str:cardno>/<str:filename>',views.panvalidation,name="panvalidation"),
  	path('aadharvali/<int:card>/<str:name>/<str:cardno>/<str:filename>',views.aadharvalidation,name="aadharvalidation"),
  	path('charts',views.charts,name="charts"),
  	path('components',views.components,name="components"),
  	path('stocks',views.stocks,name="stocks"),
  	path('gmarket',views.globalmarket,name="globalmarket"),
  	path('indices',views.indices,name="indices"),
  	path('commidities',views.commidities,name="commidities"),
  	path('forex',views.forex,name='forex'),
  	path('cryptocurrencies',views.cryptocurrencies,name="cryptocurrencies")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)