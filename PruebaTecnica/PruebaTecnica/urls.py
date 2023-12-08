
from django.contrib import admin
from django.urls import path, include
from . import vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.index , name = "index"),
    path('contacto/', vista.contacto , name = "contacto"),
    path('sobremi/', vista.sobremi , name = "sobremi"),
    path('carga/', vista.carga , name = "carga"),
    path('comentarios/', include('comentarios.urls'))
]
