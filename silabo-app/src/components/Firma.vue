<template>
  <div class="firma-upload">
    <input type="file" accept="image/jpeg, image/png" @change="handleFileUpload" />
    <div v-if="imageUrl" class="firma-preview">
      <img :src="imageUrl" alt="Firma cargada" class="firma-image" />
    </div>
    <div v-if="firmaDesdeJson" class="firma-preview">
      <img :src="firmaDesdeJson.url" alt="Firma desde JSON" class="firma-image" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrl: null,
      firmaDesdeJson: null, 
    };
  },
  created() {
    this.cargarFirmaDesdeJson();
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file && (file.type === 'image/jpeg' || file.type === 'image/png')) {
        const reader = new FileReader();
        reader.onload = () => {
          this.imageUrl = reader.result;
        };
        reader.readAsDataURL(file);
      } else {
        alert('Por favor, cargue una imagen en formato JPG o PNG');
      }
    },
    cargarFirmaDesdeJson() {
      const jsonData = {
        firma: {
          url: '/Firma.png',
        },
      };
      this.firmaDesdeJson = jsonData.firma;
    },
  },
};
</script>

<style scoped>
@import '../assets/css/Firma.css';
</style>
