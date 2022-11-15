from django.contrib import admin

from .models import Equipo, Jugador, Manager

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Manager)
