<template>
  <div class="competencia-curso">
    <h3>Al término del presente curso, el estudiante estará en condiciones de:</h3>
    <div class="form-row" v-for="(competencia, index) in competencias" :key="index">
      <label :for="'competencia' + index">Competencia {{ index + 1 }}:</label>

      <!-- Textarea que se ajusta automáticamente al tamaño -->
      <textarea
        v-model="competencias[index]"
        :id="'competencia' + index"
        placeholder="Escribe la competencia"
        @input="ajustarAltura($event)"
        ref="textareas"
      ></textarea>

      <!-- Botón de eliminar al lado de la competencia -->
      <button @click="eliminarCompetencia(index)" class="eliminar" v-if="competencias.length > 1">Eliminar</button>
    </div>

    <!-- Botón para agregar nueva competencia (verde) -->
    <div class="form-row agregar-row">
      <button @click="agregarCompetencia" class="agregar">Agregar Competencia</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';

// Array con las competencias
const competencias = ref([]);

// Cargar competencias desde el JSON al montar el componente
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  
  // Cargamos las competencias del JSON
  competencias.value = data.competencias;

  // Ajustamos la altura de los textareas después de cargar los datos
  nextTick(() => {
    ajustarAltura();
  });
});

// Función para agregar una nueva competencia
const agregarCompetencia = () => {
  competencias.value.push(""); // Añadimos un string vacío como nueva competencia
};

// Función para eliminar una competencia
const eliminarCompetencia = (index) => {
  competencias.value.splice(index, 1); // Eliminar la competencia en el índice proporcionado
};

// Función para ajustar dinámicamente la altura del textarea
const ajustarAltura = (event) => {
  // Si la función fue llamada por un evento de entrada, obtenemos el textarea del evento
  const textareas = event ? [event.target] : document.querySelectorAll('textarea');

  textareas.forEach(textarea => {
    textarea.style.height = 'auto';  // Restablece la altura
    textarea.style.height = textarea.scrollHeight + 'px';  // Ajusta la altura al contenido
  });
};
</script>

<style scoped>
@import '../assets/css/CompetenciaCurso.css'; /* Importar el archivo CSS específico */
</style>
