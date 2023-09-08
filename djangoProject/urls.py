from django.contrib import admin
from django.urls import path
from Parcial1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('actualizar_grafica/', views.actualizar_grafica, name='Actualizar gráfica'),
]
