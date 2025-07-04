from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Syllabus,
    UnidadAprendizaje,
    Actividad,
    CriterioEvaluacion,
    Competencia
)

admin.site.register(Syllabus)
admin.site.register(UnidadAprendizaje)
admin.site.register(Actividad)
admin.site.register(CriterioEvaluacion)
admin.site.register(Competencia)
