

from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reserva/', PersonaCreateView.as_view()),
    path('reserva/<int:pk>/', PersonaDetailView.as_view()),


]
