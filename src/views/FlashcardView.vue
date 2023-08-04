<template>
  <main>
    <div>title: {{ set.title }}</div>
    <div @click="flipCard">card: {{ cardText }}</div>
    <div>progress: {{ cardNo + 1 }}/{{ set.flashcards.length }}</div>
    <button @click="nextCard">incorrectly</button>
    <button @click="nextCard">correctly</button>
    <br />
    <button @click="undoCard">undo</button>
    <button @click="shuffleCards">shuffle (currently {{ isShuffled ? 'on' : 'off' }})</button>
    <br />
    <button>flashcards</button>
    <button>learn</button>
    <button>test</button>
    <button>match</button>
  </main>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Ref } from 'vue'

import set from '@/assets/sets/set.json'

const cardTextState: Ref<'definition' | 'term'> = ref('definition')
const cardNo: Ref<number> = ref(0)
const unshuffledFlashcards: Ref<Array<{ term: string; definition: string }>> = ref(
  set.flashcards.slice()
)
const isShuffled: Ref<boolean> = ref(false)

const cardText = computed(() => {
  isShuffled.value
  return set.flashcards[cardNo.value][cardTextState.value]
})

const flipCard = () => {
  cardTextState.value = cardTextState.value === 'definition' ? 'term' : 'definition'
}

const nextCard = () => {
  cardNo.value = (cardNo.value + 1) % set.flashcards.length
}

const undoCard = () => {
  cardNo.value = (cardNo.value - 1) % set.flashcards.length
}

const shuffleCards = () => {
  cardNo.value = 0
  if (isShuffled.value) {
    set.flashcards = unshuffledFlashcards.value.slice()
  } else {
    for (let i = set.flashcards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      let temp = set.flashcards[i]
      set.flashcards[i] = set.flashcards[j]
      set.flashcards[j] = temp
    }
  }
  isShuffled.value = !isShuffled.value
}
</script>
