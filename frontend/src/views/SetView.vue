<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import Main from '@/components/set/SetMain.vue'
import Flashcards from '@/components/set/SetFlashcards.vue'
import set from '@/assets/sets/set.json'
import type { SceneType } from '@/types/SceneType'

const sceneState: Ref<SceneType> = ref('main')
const cardTextState: Ref<'definition' | 'term'> = ref('definition')
const cardIndex = ref(0)
const isShuffled = ref(false)

const cardText = computed(() => {
  // To force update on isShuffled value changes
  isShuffled.value
  return set.flashcards[cardIndex.value][cardTextState.value]
})

const setSceneState = (newScene: SceneType) => {
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

const updateStreak = (id: number, newStreak: number) => {
  const foundIndex = set.flashcards.findIndex((card) => card.id === id)
  set.flashcards[foundIndex].streak = newStreak
}

const shuffleCards = () => {
  cardIndex.value = 0
  if (isShuffled.value) {
    set.flashcards.sort((a, b) => a.id - b.id) // from lowest to highest id
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
  <div v-else>Error with `setState`, current value: {{ sceneState }}.</div>
</template>
