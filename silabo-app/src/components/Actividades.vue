<template>
  <div class="actividades">
    <!-- Mostrar las actividades cargadas desde el JSON -->
    <div v-for="(actividad, index) in actividades" :key="index" class="actividad-form">
      <div class="actividad-header">
        <!-- Título de la actividad a la izquierda -->
        <h3>Actividad {{ index + 1 }}</h3>

        <!-- Botón de eliminar a la derecha -->
        <button @click="eliminarActividad(index)" class="eliminar">Eliminar</button>
      </div>

      <!-- Título de la actividad -->
      <div class="form-row">
        <label for="tituloActividad">Título:</label>
        <input v-model="actividad.titulo" id="tituloActividad" placeholder="Ej: Investigación Formativa" />
      </div>

      <!-- Descripción de la actividad -->
      <div class="form-row">
        <label for="descripcionActividad">Descripción:</label>
        <textarea
          v-model="actividad.descripcion"
          placeholder="Escribe la descripción de la actividad..."
          @input="ajustarAltura"
        ></textarea>
      </div>
    </div>

    <!-- Botón para agregar una nueva actividad -->
    <div class="form-row agregar-row">
      <button @click="agregarActividad" class="agregar">Agregar Actividad</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Arreglo de actividades
const actividades = ref([]);

// Función para cargar los datos desde el archivo JSON
onMounted(async () => {
  const response = await fetch('/silabo.json'); // Asegúrate de que el archivo JSON esté accesible
  const data = await response.json();

  // Cargar las actividades del JSON
  actividades.value = data.actividades || [];
});

// Función para agregar una nueva actividad
const agregarActividad = () => {
  actividades.value.push({
    titulo: '',
    descripcion: '',
  });
};

// Función para eliminar una actividad
const eliminarActividad = (index) => {
  actividades.value.splice(index, 1); // Elimina la actividad en el índice especificado
};

// Función para ajustar dinámicamente la altura del textarea
const ajustarAltura = (event) => {
  const textarea = event.target;
  textarea.style.height = 'auto';  // Restablecer la altura
  textarea.style.height = textarea.scrollHeight + 'px';  // Ajustar a la altura del contenido
};
</script>

<style scoped>
@import '../assets/css/Actividades.css'; /* Importar el archivo CSS específico */
</style>
