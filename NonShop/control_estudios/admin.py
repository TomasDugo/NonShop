from django.contrib import admin

from control_estudios.models import Estudiante, Profesor, Entregable


admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
