<script setup lang="ts">
import { ref, onMounted } from 'vue'

import type { Ref } from 'vue'

import type { SetType } from '@/types/SetType'

import { useUrlStore } from '@/stores/url'
import { useUserStore } from '@/stores/user'

const urlStore = useUrlStore()
const userStore = useUserStore()

const sets: Ref<Array<SetType> | null> = ref(null)
const username = ref('')

onMounted(async () => {
  const response = await fetch(`${urlStore.BACKEND_API_URL}/users/${userStore.username}`)
  const data = await response.json()
  sets.value = data.sets
  username.value = data.username
})
</script>

<template>
  <main>{{ username }}'s sets</main>
  <div v-if="sets !== null">
    <li v-for="set in sets">
      <RouterLink :to="`/sets/${set.id}`">{{ set.title }}</RouterLink>
    </li>
  </div>
</template>
