import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUrlStore = defineStore('url', () => {
  const BACKEND_API_URL = ref('http://localhost:8000')
  return { BACKEND_API_URL }
})
