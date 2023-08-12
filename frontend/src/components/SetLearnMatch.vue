<script setup lang="ts">
import { computed } from 'vue'
import type { CardType } from '@/types/CardType'

const props = defineProps(['set', 'updateStreak', 'cardIndex'])

const card = computed(() => {
  const foundIndex = props.set.flashcards.findIndex(
    (_card: CardType) => _card.id === props.cardIndex
  )
  return props.set.flashcards[foundIndex]
})
</script>

<template>
  <p>{{ card }}</p>
  <button @click="updateStreak(0, 10)">test</button>
</template>
