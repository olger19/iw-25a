# Proyecto Django - lab08

| NOMBRE DEL ALUMNO | Olger Quispe Vilca      | SEMESTRE: 8|
|-------------------|------------------------|-----------|
| **CURSO**         | Ingenieria Web         |           |
| **DOCENTE**       | Richart Smith Escobedo Quispe |     |

<span>
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white">
</span>

## Descripción

Este proyecto es una aplicación web desarrollada con Django, donde usamos Django REST Framework para realizar la practica de estudiar Rest Framework en un Proyecto Django e instalar rest_framework para enviar(POST, PUT, DELETE) y recibir (GET) mediante JSON. Permite la gestión de estudiantes, cursos, docentes, inscripciones y cargas académicas.

## Estructura del proyecto

```
lab08/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── MyDjangoProject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── MyWebApps/
    └── MyFirstApplication/
        ├── models/
        ├── admin.py
        ├── serializers.py
        ├── urls.py
        └── ...
```

## Instalación y ejecución

### 1. Crear y activar un entorno virtual

En la carpeta `lab08`:

**Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```sh
pip install -r requirements.txt
```

### 3. Aplicar migraciones

```sh
python manage.py migrate
```

### 4. Ejecutar el servidor de desarrollo

```sh
python manage.py runserver
```

- API REST: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## Notas

- Si usas VS Code, selecciona el intérprete de Python del entorno virtual para evitar errores de importación.
- El archivo [`requirements.txt`](requirements.txt) contiene las dependencias necesarias.
- Configuración principal en [`MyDjangoProject/settings.py`](MyDjangoProject/settings.py).

---

© 2025 Olger Quispe Vilca