from django.conf import settings
from django.conf.urls.static import static



from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.edit_video),
    path('black/',views.black),
    path('paint/',views.paint),
    path('Mirror_x/',views.mirrorx),
    path('Mirror_y/',views.mirrory),
   
    path('invertcolors/',views.invertcolors),
    path('lumcontrast/',views.lumcontrast),
    path('evensize/',views.evensize),
    path('timemirror/',views.timemirror),
  
   path('trim/',views.trim_edit),

   path('show/',views.show),
  path('sid/',views.sid),
  path("form/",views.form),
]


if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
