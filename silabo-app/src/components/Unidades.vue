<template>
  <div class="unidades">
    <!-- Mostrar las unidades -->
    <div v-for="(unidad, index) in unidades" :key="index" class="unidad-form">
      <!-- Contenedor de la unidad con header -->
      <div class="unidad-header">
        <h2>Unidad {{ numeroARomano(index + 1) }}</h2>
        <!-- Botón para eliminar unidad -->
        <button v-if="unidades.length > 1" @click="eliminarUnidad(index)" class="eliminar">Eliminar Unidad</button> <!-- Asegura que no se pueda eliminar la última unidad -->
      </div>

      <!-- Campos de la unidad -->
      <div class="form-row">
        <div class="columna">
          <label for="fechaInicio">Intervalo de Fechas:</label>
          <div>
            <label for="fechaInicio">Fecha de Inicio:</label>
            <input v-model="unidad.fechaInicio" type="date" id="fechaInicio" @change="calcularSemanas(index)" />
          </div>
          <div>
            <label for="fechaFin">Fecha de Fin:</label>
            <input v-model="unidad.fechaFin" type="date" id="fechaFin" @change="calcularSemanas(index)" />
          </div>
        </div>

        <div class="columna">
          <label for="denominacion">Denominación:</label>
          <textarea v-model="unidad.denominacion" id="denominacion" placeholder="Denominación de la unidad" @input="ajustarAltura"></textarea>
        </div>

        <div class="columna">
          <label for="enunciado">Enunciado de la capacidad a ser lograda:</label>
          <textarea v-model="unidad.enunciado" id="enunciado" placeholder="Enunciado de la unidad" @input="ajustarAltura"></textarea>
        </div>
      </div>

      <h3>Semanas de la Unidad:</h3>

      <!-- Semanas de la unidad -->
      <div v-for="(semana, index) in unidad.semanas" :key="index" class="semana">
        <div class="semana-header">
          <!-- Mostrar el número de semana correctamente -->
          <label>Semana {{ semana.numero }}:</label>
          <button v-if="index !== 8 && index !== 16" @click="eliminarSemana(index, unidad)" class="eliminar">Eliminar</button>
        </div>

        <!-- Contenido de la semana -->
        <div v-if="index !== 8 && index !== 16">
          <textarea v-model="semana.contenido" placeholder="Contenido de la semana" @input="ajustarAltura"></textarea>
        </div>

        <!-- Examen Parcial y Final -->
        <div v-else>
          <textarea disabled v-model="semana.contenido" placeholder="Contenido de la semana">
            {{ index === 8 ? 'Examen Parcial' : 'Examen Final' }}
          </textarea>
        </div>
      </div>

      <!-- Botón para agregar una semana -->
      <button v-if="totalSemanas < 17 && unidad.semanas.length < 17" @click="agregarSemana(index)">Agregar Semana</button>

      <!-- Otros campos de la unidad (Metodología, Fuentes de Consulta) -->
      <div class="form-row-doble">
        <div>
          <label for="metodologia">Metodología:</label>
          <textarea v-model="unidad.metodologia" id="metodologia" placeholder="Metodología utilizada" @input="ajustarAltura"></textarea>
        </div>

        <div>
          <label for="fuentes">Fuentes de Consulta:</label>
          <textarea v-model="unidad.fuentes" id="fuentes" placeholder="Fuentes de consulta documental" @input="ajustarAltura"></textarea>
        </div>
      </div>
    </div>

    <!-- Botón para agregar una nueva unidad -->
    <div class="form-row agregar-row">
      <button v-if="totalSemanas < 17" @click="agregarUnidad" class="agregar">Agregar Unidad</button> <!-- Solo habilitado si no se han alcanzado 17 semanas -->
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const unidades = ref([]);
let semanaContador = 1; // Variable global para llevar el contador de semanas
let totalSemanas = 0; // Total de semanas en todas las unidades

// Función para convertir números a romanos (solo hasta el 5)
function numeroARomano(num) {
  const romanNumerals = [
    { value: 5, symbol: 'V' },
    { value: 4, symbol: 'IV' },
    { value: 1, symbol: 'I' },
  ];

  let resultado = '';

  for (const { value, symbol } of romanNumerals) {
    while (num >= value) {
      resultado += symbol;
      num -= value;
    }
  }

  return resultado;
}

// Cargar los datos del JSON al montar el componente
onMounted(async () => {
  const response = await fetch('/silabo.json');
  const data = await response.json();
  unidades.value = data.unidades;

  // Reiniciar contador de semanas y total
  semanaContador = 1;
  totalSemanas = 0;

  // Inicializar el contador de semanas y el total de semanas
  for (let i = 0; i < unidades.value.length; i++) {
    for (let j = 0; j < unidades.value[i].semanas.length; j++) {
      const semana = unidades.value[i].semanas[j];
      semana.numero = semanaContador++;

      // Verificar si la semana es la 9 o la 17, y aplicarle el contenido y la propiedad disabled
      if (semana.numero === 9) {
        semana.contenido = 'Examen Parcial';
        semana.disabled = true;
      } else if (semana.numero === 17) {
        semana.contenido = 'Examen Final';
        semana.disabled = true;
      }

      totalSemanas++;
    }
  }
});

// Función para calcular las semanas en función del intervalo de fechas
const calcularSemanas = (index) => {
  const fechaInicio = new Date(unidades.value[index].fechaInicio);
  const fechaFin = new Date(unidades.value[index].fechaFin);
  const diffInTime = fechaFin.getTime() - fechaInicio.getTime();
  const diffInDays = diffInTime / (1000 * 3600 * 24);
  const numSemanas = Math.ceil(diffInDays / 7);

  // Evitar agregar más de 17 semanas en total
  if (totalSemanas + numSemanas > 17) {
    alert('El total de semanas no puede exceder de 17.');
    return;
  }

  unidades.value[index].semanas = [];
  for (let i = 0; i < numSemanas; i++) {
    const semana = {
      contenido: '',
      numero: semanaContador,
      disabled: false,  // Inicialmente no está deshabilitada
    };

    // Verificar si la semana es la 9 o la 17, y aplicarle el contenido y la propiedad disabled
    if (semana.numero === 9) {
      semana.contenido = 'Examen Parcial';
      semana.disabled = true;
    } else if (semana.numero === 17) {
      semana.contenido = 'Examen Final';
      semana.disabled = true;
    }

    unidades.value[index].semanas.push(semana);
    semanaContador++;
    totalSemanas++;
  }
};

// Función para agregar una nueva semana
const agregarSemana = (index) => {
  if (totalSemanas < 17 && unidades.value[index].semanas.length < 17) {
    const semana = {
      contenido: '',
      numero: semanaContador,
      disabled: false,  // Inicialmente no está deshabilitada
    };

    // Verificar si la semana es la 9 o la 17, y aplicarle el contenido y la propiedad disabled
    if (semana.numero === 9) {
      semana.contenido = 'Examen Parcial';
      semana.disabled = true;
    } else if (semana.numero === 17) {
      semana.contenido = 'Examen Final';
      semana.disabled = true;
    }

    unidades.value[index].semanas.push(semana);
    semanaContador++;
    totalSemanas++;
  } else {
    alert('No se pueden agregar más semanas, el total de semanas ya alcanzó el límite.');
  }
};

// Función para eliminar una semana
const eliminarSemana = (index, unidad) => {
  unidad.semanas.splice(index, 1);
  recalcularSemanaContador(); // Recalcular el contador después de eliminar una semana
  totalSemanas--;
};

// Función para eliminar una unidad
const eliminarUnidad = (index) => {
  const unidad = unidades.value[index];
  const semanasAEliminar = unidad.semanas.length;

  // Eliminar la unidad
  unidades.value.splice(index, 1);
  totalSemanas -= semanasAEliminar;

  // Recalcular el contador de semanas
  recalcularSemanaContador();
};

// Función para recalcular el contador de semanas
const recalcularSemanaContador = () => {
  // Volver a contar todas las semanas de todas las unidades
  semanaContador = 1; // Reiniciar el contador de semanas
  totalSemanas = 0;  // Reiniciar el total de semanas

  unidades.value.forEach((unidad) => {
    unidad.semanas.forEach((semana) => {
      semana.numero = semanaContador++;  // Asignar el número correcto a cada semana
      totalSemanas++;
    });
  });
};

// Función para agregar una nueva unidad
const agregarUnidad = () => {
  if (unidades.value.length < 5 && totalSemanas < 17) {
    unidades.value.push({
      fechaInicio: '',
      fechaFin: '',
      denominacion: '',
      enunciado: '',
      semanas: [],
      metodologia: '',
      fuentes: ''
    });
  } else {
    console.log("No se pueden agregar más de 5 unidades o ya se alcanzaron las 17 semanas.");
  }
};

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
@import '../assets/css/Unidades.css'; /* Importar el archivo CSS específico */
</style>
