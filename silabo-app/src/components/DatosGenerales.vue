<template>
  <div class="datos-generales">
    <div class="form-row">
        <label for="docente">Curso:</label>
      <input v-model="curso.nombre" placeholder="Nombre del curso" />
    </div>
    <div class="form-row">
        <label for="docente">Código del curso:</label>
        <input v-model="curso.codigo" placeholder="Código del curso" />
    </div>
    <div class="form-row">
      <label for="docente">Docente:</label>
      <input id="docente" v-model="curso.docente.nombre" placeholder="Docente" />
    </div>
    <div class="form-row">
      <label for="semestre">Semestre:</label>
      <input id="semestre" v-model="curso.semestre" placeholder="Semestre" />
    </div>
    <div class="form-row">
      <label for="facultad">Facultad:</label>
      <input id="facultad" v-model="curso.facultad" placeholder="Facultad" />
    </div>
    <div class="form-row">
      <label for="area_formacion">Área de formación:</label>
      <input id="area_formacion" v-model="curso.area_formacion" placeholder="Área de formación" />
    </div>
    <div class="form-row">
      <label for="tipo_curso">Tipo de curso:</label>
      <input id="tipo_curso" v-model="curso.tipo_curso" placeholder="Tipo de curso" />
    </div>
    <div class="form-row">
      <label for="carrera_profesional">Carrera profesional:</label>
      <input id="carrera_profesional" v-model="curso.carrera_profesional" placeholder="Carrera profesional" />
    </div>
    <div class="form-row">
      <label for="creditos">Créditos:</label>
      <input id="creditos" v-model="curso.creditos" type="number" placeholder="Créditos" />
    </div>
    <div class="form-row">
      <label for="prerequisito">Prerequisito:</label>
      <input id="prerequisito" v-model="curso.prerequisito" placeholder="Prerequisito" />
    </div>
    <div class="form-row">
      <label for="periodo_lectivo">Periodo lectivo:</label>
      <input id="periodo_lectivo" v-model="curso.periodo_lectivo" placeholder="Periodo lectivo" />
    </div>
    <div class="form-row">
      <label for="horas_practica">Horas prácticas:</label>
      <input id="horas_practica" v-model="curso.horas.practica" type="number" placeholder="Horas prácticas" />
    </div>
    <div class="form-row">
      <label for="horas_teoria">Horas teóricas:</label>
      <input id="horas_teoria" v-model="curso.horas.teoria" type="number" placeholder="Horas teóricas" />
    </div>
    <div class="form-row">
      <label for="correo_docente">Correo del docente:</label>
      <input id="correo_docente" v-model="curso.docente.correo" placeholder="Correo del docente" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const curso = ref({
  nombre: '',
  codigo: '',
  semestre: '',
  facultad: '',
  area_formacion: '',
  tipo_curso: '',
  carrera_profesional: '',
  creditos: 0,
  prerequisito: '',
  periodo_lectivo: '',
  horas: {
    teoria: 0,
    practica: 0
  },
  docente: {
    nombre: '',
    correo: ''
  },
  fecha_inicio: '',
  fecha_fin: ''
});

// Cargar el JSON del sílabo
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  
  // Accedemos solo a los datos de 'curso' en el JSON
  curso.value = data.curso;
});
</script>

<style src="../assets/css/DatosGenerales.css"></style>
