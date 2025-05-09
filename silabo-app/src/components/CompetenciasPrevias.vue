<template>
  <div class="competencias-previas">
    <!-- Texto inicial para el estudiante -->
    <h3>Antes de iniciar el curso, el estudiante debería:</h3>

    <div class="form-row" v-for="(competencia, index) in competenciasPrevias" :key="index">
      <label :for="'competenciaPrevia' + index">Competencia {{ index + 1 }}:</label>

      <!-- Textarea para la competencia previa -->
      <textarea
        v-model="competenciasPrevias[index]"
        :id="'competenciaPrevia' + index"
        placeholder="Escribe la competencia previa necesaria"
        @input="ajustarAltura"
      ></textarea>

      <!-- Botón de eliminar al lado de la competencia -->
      <button @click="eliminarCompetencia(index)" class="eliminar" v-if="competenciasPrevias.length > 1">Eliminar</button>
    </div>

    <!-- Botón para agregar nueva competencia previa -->
    <div class="form-row agregar-row">
      <button @click="agregarCompetencia" class="agregar">Agregar Competencia</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';

// Array con las competencias previas
const competenciasPrevias = ref([]);

// Cargar competencias previas desde el JSON al montar el componente
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  
  // Cargamos las competencias previas necesarias desde el JSON
  competenciasPrevias.value = data.competenciasPrevias;

  // Ajustamos la altura de los textareas después de cargar los datos
  nextTick(() => {
    ajustarAltura();
  });
});

// Función para agregar una nueva competencia previa
const agregarCompetencia = () => {
  competenciasPrevias.value.push(""); // Añadimos un string vacío como nueva competencia previa
};

// Función para eliminar una competencia previa
const eliminarCompetencia = (index) => {
  competenciasPrevias.value.splice(index, 1); // Eliminar la competencia en el índice proporcionado
};

// Función para ajustar dinámicamente la altura del textarea
const ajustarAltura = (event) => {
  const textareas = event ? [event.target] : document.querySelectorAll('textarea');

  textareas.forEach(textarea => {
    textarea.style.height = 'auto';  // Restablece la altura
    textarea.style.height = textarea.scrollHeight + 'px';  // Ajusta la altura al contenido
  });
};
</script>

<style scoped>
@import '../assets/css/CompetenciasPrevias.css'; /* Importar el archivo CSS específico */
</style>
