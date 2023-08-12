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
  <div>description: {{ set.description }}</div>
  <div @click="flipCard">card: {{ cardText }}</div>
  <div>progress: {{ cardIndex + 1 }}/{{ set.flashcards.length }}</div>
  <button @click="nextCard" :disabled="cardIndex + 1 === set.flashcards.length">incorrectly</button>
  <button @click="nextCard" :disabled="cardIndex + 1 === set.flashcards.length">correctly</button>
  <br />
  <button @click="prevCard" :disabled="cardIndex === 0">undo</button>
  <button @click="shuffleCards">shuffle (currently {{ isShuffled ? 'on' : 'off' }})</button>
  <br />
  <button @click="setSceneState('flashcards')">flashcards</button>
  <button @click="setSceneState('learn')">learn</button>
  <button @click="setSceneState('test')" disabled>test (not implemented)</button>
</template>
