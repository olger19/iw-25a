<template>
  <div class="competencia-perfil">  
    <!-- Textarea para mostrar y editar la competencia -->
    <textarea
      v-model="competenciaPerfilEgreso"
      id="competenciaPerfilEgreso"
      placeholder="Escribe la competencia del perfil de egreso"
      @input="ajustarAltura"
    ></textarea>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';

// Definimos la competencia del perfil de egreso
const competenciaPerfilEgreso = ref('');

// Cargar la competencia desde el JSON al montar el componente
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  
  // Cargamos la competencia del perfil de egreso desde el JSON
  competenciaPerfilEgreso.value = data.competenciaEgreso;

  // Ajustamos la altura del textarea después de cargar el contenido
  nextTick(() => {
    ajustarAltura();
  });
});

// Función para ajustar dinámicamente la altura del textarea
const ajustarAltura = () => {
  const textarea = document.getElementById('competenciaPerfilEgreso');
  textarea.style.height = 'auto';  // Restablece la altura
  textarea.style.height = textarea.scrollHeight + 'px';  // Ajusta la altura al contenido
};
</script>

<style scoped>
@import '../assets/css/CompetenciaPerfilEgreso.css'; /* Importar el archivo CSS específico */
</style>
