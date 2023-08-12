<script setup lang="ts">
const props = defineProps(['set', 'updateStreak'])
</script>

<template>
  <p>{{ set.flashcards[0] }}</p>
  <button @click="updateStreak(0, 10)">test</button>
</template>
