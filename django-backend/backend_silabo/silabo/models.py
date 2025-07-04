
# Create your models here.
from django.db import models

class Syllabus(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    anio = models.CharField(max_length=20)
    docente_nombre = models.CharField(max_length=200)
    docente_correo = models.EmailField()
    firma_docente = models.URLField(blank=True, null=True)
    periodo_lectivo = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo or 'Syllabus'} - {self.anio}"

class UnidadAprendizaje(models.Model):
    syllabus = models.ForeignKey(Syllabus, related_name="unidades", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    semana_inicio = models.IntegerField()
    semana_fin = models.IntegerField()
    objetivo = models.TextField()
    contenidos = models.TextField()

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    syllabus = models.ForeignKey(Syllabus, related_name="actividades", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

class CriterioEvaluacion(models.Model):
    syllabus = models.ForeignKey(Syllabus, related_name="criterios", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ponderacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class Competencia(models.Model):
    syllabus = models.ForeignKey(Syllabus, related_name="competencias", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)  # general / egreso / previa
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo}: {self.descripcion[:30]}"
