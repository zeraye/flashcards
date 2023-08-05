<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import Main from '@/components/SetMain.vue'
import Flashcards from '@/components/SetFlashcards.vue'
import Learn from '@/components/SetLearn.vue'
import Test from '@/components/SetTest.vue'
import Match from '@/components/SetMatch.vue'
import set from '@/assets/sets/set.json'

const sceneState: Ref<'main' | 'flashcards' | 'learn' | 'test' | 'match'> = ref('main')
const cardTextState: Ref<'definition' | 'term'> = ref('definition')
const cardIndex = ref(0)
const isShuffled = ref(false)
const unshuffledFlashcards = set.flashcards.slice()

const cardText = computed(() => {
  // To force update on isShuffled value changes
  isShuffled.value
  return set.flashcards[cardIndex.value][cardTextState.value]
})

const setSceneState = (newScene: 'main' | 'flashcards' | 'learn' | 'test' | 'match') => {
  sceneState.value = newScene
}

const flipCard = () => {
  cardTextState.value = cardTextState.value === 'definition' ? 'term' : 'definition'
}

const nextCard = () => {
  cardIndex.value = (cardIndex.value + 1) % set.flashcards.length
}

const prevCard = () => {
  if (cardIndex.value > 0) cardIndex.value--
}

const shuffleCards = () => {
  cardIndex.value = 0
  if (isShuffled.value) {
    set.flashcards = unshuffledFlashcards.slice()
  } else {
    for (let i = set.flashcards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      let tmp = set.flashcards[i]
      set.flashcards[i] = set.flashcards[j]
      set.flashcards[j] = tmp
    }
  }
  isShuffled.value = !isShuffled.value
}
</script>

<template>
  <Main
    v-if="sceneState === 'main'"
    :set="set"
    :setSceneState="setSceneState"
    :flipCard="flipCard"
    :nextCard="nextCard"
    :prevCard="prevCard"
    :shuffleCards="shuffleCards"
    :cardText="cardText"
    :cardIndex="cardIndex"
    :isShuffled="isShuffled"
  />
  <Flashcards
    v-else-if="sceneState === 'flashcards'"
    :set="set"
    :setSceneState="setSceneState"
    :flipCard="flipCard"
    :nextCard="nextCard"
    :prevCard="prevCard"
    :shuffleCards="shuffleCards"
    :cardText="cardText"
    :cardIndex="cardIndex"
    :isShuffled="isShuffled"
  />
  <Learn v-else-if="sceneState === 'learn'" :setSceneState="setSceneState" />
  <Test v-else-if="sceneState === 'test'" :setSceneState="setSceneState" />
  <Match v-else-if="sceneState === 'match'" :setSceneState="setSceneState" />
  <div v-else>Error with `setState`, current value: {{ sceneState }}.</div>
</template>
