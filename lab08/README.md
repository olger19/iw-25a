# PRACTICA JWT CON DJANGO

**En este ejercicio probaremos todos los metodos enfocados en Cursos mediante token JWT.**

## 🚀 Requisitos previos

- Python instalado
- `pip install requests` (si se usará `test_api_examples.py`)
- Servidor Django corriendo en: `http://127.0.0.1:8000/`
- Base de datos migrada y con modelos activos
- Postman para probar endpoints

## Configuracion JWT con Django REST FRAMEWROK 

1️⃣ Instalar librería JWT

```bash
pip install djangorestframework-simplejwt
```

2️⃣ Configurar settings.py

Abre tu archivo: `MyDjangoProject/settings.py`

Agrega (o edita), su settings debe tener lo siguiente:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Opcional: proteger por defecto
    )
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'rest_framework_simplejwt',  # JWT Authentication ADD
    'MyWebApps.MyFirstApplication',
]

# JWT Authentication Settings ADD
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),  # puedes cambiar el tiempo que quieras ADD
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),    # refresh token duración para sacar un nuevo acces token ADD
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```
3️⃣ Agregar las rutas JWT en tu urls.py global

Tu urls.py global debería estar en: `MyDjangoProject/urls.py`

Agrega esto al inicio:
```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
```

Y en tu urlpatterns, agrega:
```python
urlpatterns = [
    # tus otras rutas

    # Rutas para JWT:
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Incluye tus apps:
    path('myapp/', include('MyWebApps.MyFirstApplication.urls')),  # ejemplo
]
```

4️⃣ Cómo usarlo
👉 Paso 1: Obtener token
Haces un POST a:
```bash
http://127.0.0.1:8000/api/token/
```

Con body:
``` json
{
    "username": "admin",
    "password": "1234"
}

```

👉 Paso 2: El servidor responde:
```json
{
    "access": "jwt_token_aqui",
    "refresh": "refresh_token_aqui"
}
```

👉 Paso 3: Usa el token en las cabeceras de tus peticiones:
```makefile
Authorization: Bearer jwt_token_aqui
```

Por ultimo agregue a las vistas de Courses: 

```python
from rest_framework.permissions import IsAuthenticated

```
y

```python
permission_classes = [IsAuthenticated]
```

---

## 📁 Postman 

Se incluye los metodos para probar en postman, no se olvide de agregar el token jwt a postman:

1. **Listar Cursos**
 - `GET http://127.0.0.1:8000/api/courses/`

2. **Crear Curso**
 - `POST http://127.0.0.1:8000/api/courses/`
 - JSON de ejemplo:
   ```json
   {
     "curriculum": 2023,
     "year": 3,
     "semester": 5,
     "code": "CUR405",
     "name": "como usar rest",
     "acronym": "PROG-WEB",
     "credits": 4.0,
     "theory_hours": 2.0,
     "practice_hours": 2.0,
     "laboratory_hours": 2.0,
     "laboratory": true
   }
   ```
3. **Actualizar Curso**
- `PUT http://127.0.0.1:8000/api/courses/af0262e6-f1ca-4dec-9353-cc5a10f10656/`

4. **Eliminar Curso**
- `DELETE http://127.0.0.1:8000/api/courses/af0262e6-f1ca-4dec-9353-cc5a10f10656/`

3. **Crear Profesor**
 - `POST http://127.0.0.1:8000/api/teachers/`
 - JSON de ejemplo:
   ```json
   {
     "names": "Juan Carlos",
     "father_surname": "Gomez Boza",
     "mother_surname": "López",
     "email": "juan.gomez@universidad.edu",
     "phone": "+51987654321",
     "show_phone": true
   }
   ```

4. **Actualizar Profesor**
 - `PUT http://127.0.0.1:8000/api/teachers/1/`
 - JSON de ejemplo:
   ```json
   {
     "names": "Juan Carlos",
     "father_surname": "García",
     "mother_surname": "López",
     "email": "juancarlos.actualizado@universidad.edu",
     "phone": "+51987654321",
     "show_phone": false
   }
   ```

5. **Eliminar Profesor**
 - `DELETE http://127.0.0.1:8000/api/teachers/1/`

6. **Crear Estudiante**
 - `POST http://127.0.0.1:8000/api/students/`
 - JSON de ejemplo:
   ```json
   {
     "cui": 20220001,
     "names": "Marycielo",
     "father_surname": "Bedoya",
     "mother_surname": "Pinto",
     "email": "marycielo.bedoya@estudiante.edu",
     "phone": "+51987123456"
   }
   ```

7. **Crear Carga de Trabajo**
 - `POST http://127.0.0.1:8000/api/workloads/`
 - JSON de ejemplo:
   ```json
   {
     "course": 2,
     "group": "A",
     "laboratory": "lab01",
     "capacity": 25,
     "teacher": 2
   }
   ```

8. **Crear Inscripción**
 - `POST http://127.0.0.1:8000/api/inscriptions/`
 - JSON esperado:
   ```json
   {
     "workload": 2,
     "student": 1
   }
   ```

---

## ✍ Autor

Olger Quispe Vilca  
GitHub: [@olger19](https://github.com/olger19)
