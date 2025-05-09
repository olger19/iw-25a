<template>
  <div class="app">
    <header class="header">
      <h1>Sílabos ULASALLE</h1>
    </header>
    <section class="content">
      <h2>DATOS GENERALES</h2>
      <DatosGenerales />
    </section>
    <section class="content">
      <h2>COMPETENCIA DEL CURSO</h2>
      <CompetenciaCurso/>
    </section>
    <section class="content">
      <h2>COMPETENCIA DEL PERFIL DE EGRESO AL QUE CONTRIBUYE</h2>
      <CompetenciaPerfilEgresado/>
    </section>
    <section class="content">
      <h2>COMPETENCIAS PREVIAS NECESARIAS</h2>
      <CompetenciasPrevias/>
    </section>
    <section class="content">
      <h2>SUMILLA</h2>
      <Sumilla/>
    </section>
    <section class="content">
      <h2>UNIDADES DE APRENDIZAJE</h2>
      <Unidades/>
    </section>
    <section class="content">
      <h2>ACTIVIDADES</h2>
      <Actividades/>
    </section>
    <section class="content">
      <h2>CRITERIOS DE EVALUACIÓN</h2>
      <CriteriosEvaluación/>
    </section>
    <section class="content">
      <h2>FIRMA DEL DOCENTE</h2>
      <h4>Ingrese su firma en formato JPG o PNG.</h4>
      <Firma/>
    </section>

    <!-- Botón para generar y descargar el JSON -->
    <button @click="exportarJSON">Exportar JSON</button>
  </div>
</template>

<script setup>
import Actividades from './components/Actividades.vue';
import CompetenciaCurso from './components/CompetenciaCurso.vue';
import CompetenciaPerfilEgresado from './components/CompetenciaPerfilEgreso.vue';
import CompetenciasPrevias from './components/CompetenciasPrevias.vue';
import CriteriosEvaluación from './components/CriteriosEvaluación.vue';
import DatosGenerales from './components/DatosGenerales.vue';
import Firma from './components/Firma.vue';
import Sumilla from './components/Sumilla.vue';
import Unidades from './components/Unidades.vue';

</script>

<style scoped>
</style>
