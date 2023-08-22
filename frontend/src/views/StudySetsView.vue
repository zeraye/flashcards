<script setup lang="ts">
import { ref, onMounted } from 'vue'

import type { Ref } from 'vue'

import type { SetType } from '@/types/SetType'

import { useUrlStore } from '@/stores/url'
import { useUserStore } from '@/stores/user'

import { useRoute } from 'vue-router'

const urlStore = useUrlStore()
const userStore = useUserStore()

const sets: Ref<Array<SetType> | null> = ref(null)
const username = ref(useRoute().params.user ?? userStore.username)

onMounted(async () => {
  const response = await fetch(`${urlStore.BACKEND_API_URL}/users/${username.value}`)
  const data = await response.json()
  sets.value = data.sets ?? []
})
</script>

<template>
  <main>{{ username }}'s sets</main>
  <div v-if="sets !== null">
    <p v-if="sets.length === 0">user has no sets</p>
    <li v-for="set in sets">
      <RouterLink :to="`/set/${set.id}`">{{ set.title }}</RouterLink>
    </li>
  </div>
</template>
