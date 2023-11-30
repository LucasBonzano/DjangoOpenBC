
from django.contrib import admin
from django.urls import path
from . import vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.index , name = "index"),
    path('contacto/', vista.contacto , name = "contacto"),
    path('sobremi/', vista.sobremi , name = "sobremi"),
]
