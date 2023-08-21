<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import type { Ref } from 'vue'
import Main from '@/components/set/SetMain.vue'
import Flashcards from '@/components/set/SetFlashcards.vue'
import type { SceneType } from '@/types/SceneType'
import type { SetType } from '@/types/SetType'

import { useUrlStore } from '@/stores/url'

const urlStore = useUrlStore()

const sceneState: Ref<SceneType> = ref('main')
const cardTextState: Ref<'definition' | 'term'> = ref('definition')
const cardIndex = ref(0)
const isShuffled = ref(false)

const set: Ref<SetType | null> = ref(null)

onMounted(async () => {
  const response = await fetch(`${urlStore.BACKEND_API_URL}/sets/${useRoute().params.id}`)
  const data = await response.json()
  set.value = data
})

const cardText = computed(() => {
  if (set.value === null) return
  // To force update on isShuffled value changes
  isShuffled.value
  return set.value.flashcards[cardIndex.value][cardTextState.value]
})

const setSceneState = (newScene: SceneType) => {
  sceneState.value = newScene
}

const flipCard = () => {
  cardTextState.value = cardTextState.value === 'definition' ? 'term' : 'definition'
}

const nextCard = () => {
  if (set.value === null) return
  cardIndex.value = (cardIndex.value + 1) % set.value.flashcards.length
}

const prevCard = () => {
  if (cardIndex.value > 0) cardIndex.value--
}

const updateStreak = (id: number, newStreak: number) => {
  if (set.value === null) return
  const foundIndex = set.value.flashcards.findIndex((card) => card.id === id)
  set.value.flashcards[foundIndex].streak = newStreak
}

const shuffleCards = () => {
  if (set.value === null) return
  cardIndex.value = 0
  if (isShuffled.value) {
    set.value.flashcards.sort((a, b) => a.id - b.id) // from lowest to highest id
  } else {
    for (let i = set.value.flashcards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      let tmp = set.value.flashcards[i]
      set.value.flashcards[i] = set.value.flashcards[j]
      set.value.flashcards[j] = tmp
    }
  }
  isShuffled.value = !isShuffled.value
}
</script>

<template>
  <Main
    v-if="sceneState === 'main' && set !== null"
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
    v-else-if="sceneState === 'flashcards' && set !== null"
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
