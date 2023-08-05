<script setup lang="ts">
const props = defineProps([
  'set',
  'flipCard',
  'nextCard',
  'prevCard',
  'shuffleCards',
  'cardText',
  'cardIndex',
  'isShuffled',
  'setSceneState'
])
</script>

<template>
  <div>title: {{ set.title }}</div>
  <div @click="flipCard">card: {{ cardText }}</div>
  <div>progress: {{ cardIndex + 1 }}/{{ set.flashcards.length }}</div>
  <button @click="nextCard">incorrectly</button>
  <button @click="nextCard">correctly</button>
  <br />
  <button @click="prevCard" :disabled="cardIndex <= 0">undo</button>
  <button @click="shuffleCards">shuffle (currently {{ isShuffled ? 'on' : 'off' }})</button>
  <br />
  <button @click="setSceneState('main')">back</button>
</template>
