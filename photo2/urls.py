from django.contrib import admin
from django.urls import path,include
from photo2 import views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('',views.home,name='home'),
    path('bir',views.bir,name='bir'),
    path('ins',views.ins,name='ins'),
    path('nat',views.nat,name='nat'),
    path('tra',views.tra,name='tra'),
    path('rept',views.rept,name='rept'),
    
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  