
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Syllabus
from .serializers import SyllabusSerializer
from .models import UnidadAprendizaje
from .serializers import UnidadAprendizajeSerializer
from .models import CriterioEvaluacion
from .serializers import CriterioEvaluacionSerializer
from .models import Actividad
from .serializers import ActividadSerializer
from .models import Competencia
from .serializers import CompetenciaSerializer
# Create your views here.
# Con en este ModelViewSet ya tenemos todas las operaciones CRUD disponibles para Syllabus
class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all() # Obtiene todos los syllabus
    serializer_class = SyllabusSerializer
    permission_classes = [IsAuthenticated]  # Definir permisos si es necesario

    def get_queryset(self):
        queryset = Syllabus.objects.all()
        email = self.request.query_params.get('docente_correo')
        if email:
            queryset = queryset.filter(docente_correo=email)
        return queryset

class UnidadAprendizajeViewSet(viewsets.ModelViewSet):
    queryset = UnidadAprendizaje.objects.all()
    serializer_class = UnidadAprendizajeSerializer
    permission_classes = [IsAuthenticated]

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    permission_classes = [IsAuthenticated]

class CriterioEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = CriterioEvaluacion.objects.all()
    serializer_class = CriterioEvaluacionSerializer
    permission_classes = [IsAuthenticated]

class CompetenciaViewSet(viewsets.ModelViewSet):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer
    permission_classes = [IsAuthenticated]
