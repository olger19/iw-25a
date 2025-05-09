<template>
  <div class="criterios-evaluacion">
    <table>
      <thead>
        <tr>
          <th>Evaluación</th>
          <th>Descripción de la evaluación</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(criterio, index) in criteriosEvaluacion" :key="index">
          <td>{{ criterio.evaluacion }}</td>
          <td>
            <textarea 
              v-model="criterio.descripcion" 
              placeholder="Descripción de la evaluación"
              @input="ajustarAltura"
            ></textarea>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Arreglo de criterios de evaluación
const criteriosEvaluacion = ref([]);

// Cargar los criterios de evaluación desde el JSON al montar el componente
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  criteriosEvaluacion.value = data.criterios_evaluacion;  // Cargar los criterios desde el JSON
});

// Ajuste de altura para los textarea
const ajustarAltura = (event) => {
  const textareas = event ? [event.target] : document.querySelectorAll('textarea');

  textareas.forEach(textarea => {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
  });
};
</script>
<style scoped>
@import '../assets/css/CriteriosEvaluacion.css';
</style>
