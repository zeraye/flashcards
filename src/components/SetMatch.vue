<script setup lang="ts">
const props = defineProps(['setSceneState'])
</script>

<template>
  <p>match</p>
  <button @click="setSceneState('main')">back</button>
</template>
