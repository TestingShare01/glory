<template>
  <div>
    <app-head></app-head>
    <app-navigation></app-navigation>
    <app-preview></app-preview>
  </div>

</template>

<script>
import AppHead from "@/components/header.vue";
import AppNavigation from "@/components/navigation.vue";
import AppPreview from "@/components/preview.vue";
export default {
  components: {
    AppHead,
    AppNavigation,
    AppPreview,
  },
};
</script>

<style scoped>
.head {
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  height: 40px;
  background-color: #84c1ff;
}
.navigation {
  position: absolute;
  left: 0px;
  top: 40px;
  width: 200px;
  bottom: 0px;
  position: fixed;
  overflow-y: auto;
  overflow: hidden;
  background-color: #545c64;
}
.preview {
  position: absolute;
  top: 40px;
  left: 200px;
  right: 0px;
  bottom: 0px;
  overflow-y: auto;
  overflow-x: auto;
}

</style>