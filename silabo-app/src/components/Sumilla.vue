<template>
  <div class="sumilla">
    <!-- Textarea para la sumilla -->
    <textarea
      v-model="sumilla"
      id="sumilla"
      placeholder="Escribe la sumilla del curso"
      @input="ajustarAltura"
    ></textarea>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';

// Definimos la sumilla
const sumilla = ref('');

// Cargar la sumilla desde el JSON al montar el componente
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  
  // Cargamos la sumilla desde el JSON
  sumilla.value = data.sumilla;

  // Ajustamos la altura del textarea después de cargar los datos
  nextTick(() => {
    ajustarAltura();
  });
});

// Función para ajustar dinámicamente la altura del textarea
const ajustarAltura = (event) => {
  const textarea = event ? event.target : document.getElementById('sumilla');

  textarea.style.height = 'auto';  // Restablece la altura
  textarea.style.height = textarea.scrollHeight + 'px';  // Ajusta la altura al contenido
};
</script>

<style scoped>
@import '../assets/css/Sumilla.css'; /* Importar el archivo CSS específico */
</style>
