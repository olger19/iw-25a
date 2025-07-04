from rest_framework import serializers
from .models import (
    Syllabus,
    UnidadAprendizaje,
    Actividad,
    CriterioEvaluacion,
    Competencia
)

class UnidadAprendizajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadAprendizaje
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class CriterioEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriterioEvaluacion
        fields = '__all__'

class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'

class SyllabusSerializer(serializers.ModelSerializer):
    unidades = UnidadAprendizajeSerializer(many=True, read_only=True)
    actividades = ActividadSerializer(many=True, read_only=True)
    criterios = CriterioEvaluacionSerializer(many=True, read_only=True)
    competencias = CompetenciaSerializer(many=True, read_only=True)

    class Meta:
        model = Syllabus
        fields = '__all__'
