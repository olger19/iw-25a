from rest_framework import serializers
from .models.Student import Student  # importa el modelo correctamente

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # especificar campos id, name
