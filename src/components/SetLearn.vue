<script setup lang="ts">
import { ref, computed } from 'vue'
import SetLearnMatch from '@/components/SetLearnMatch.vue'

const props = defineProps(['setSceneState', 'set', 'updateStreak'])
</script>

<template>
  <SetLearnMatch :set="set" :updateStreak="updateStreak" />
  <button @click="setSceneState('main')">back</button>
</template>
