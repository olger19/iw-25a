from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompetenciaViewSet, CriterioEvaluacionViewSet, SyllabusViewSet
from .views import UnidadAprendizajeViewSet
from .views import ActividadViewSet

router = DefaultRouter()
router.register(r'syllabus', SyllabusViewSet)  
router.register(r'unidadaprendizaje', UnidadAprendizajeViewSet)
router.register(r'actividades', ActividadViewSet)
router.register(r'criterios', CriterioEvaluacionViewSet)
router.register(r'competencias', CompetenciaViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

