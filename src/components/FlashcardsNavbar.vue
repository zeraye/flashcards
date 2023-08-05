<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Flashcards</RouterLink>
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/sets">Study sets</RouterLink></li>
        <li><RouterLink to="/set">Set</RouterLink></li>
      </ul>
    </nav>
  </header>
</template>
