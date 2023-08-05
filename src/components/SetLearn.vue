<script setup lang="ts">
const props = defineProps(['setSceneState'])
</script>

<template>
  <p>learn</p>
  <button @click="setSceneState('main')">back</button>
</template>
