# 4 Formas de aplicar estilos

| NOMBRE DEL ALUMNO | Olger Quispe Vilca      | SEMESTRE: 8|
|-------------------|----------------------------------|-----------|
| **CURSO**        | Ingenieria Web |           |
| **DOCENTE**      | Richart Smith Escobedo Quispe      |           |

<span> 
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
</span> 

## Introducción

# Desplegar pagina estatica con con Lighttpd

## Introducción

Este proyecto despliega una página web estática utilizando **Lighttpd** dentro de un contenedor Docker.  
Se muestran ejemplos de las 4 formas de aplicar estilos en HTML: Inline, Interno, Externo y usando JavaScript.

---

## 🐳 Comandos para ejecutar

```bash
docker build . -t lighttpd_lab02
```

```bash copy
docker run -d --name web_lab02 -p 8096:80 lighttpd_lab02
```

## 🌐 Acceso a la página

En la misma máquina:

```
http://localhost:8096
```

© 2025 Olger Quispe Vilca
