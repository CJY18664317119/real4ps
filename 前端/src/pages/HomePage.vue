<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const navigateTo = (path) => {
  router.push(path)
}
</script>

<template>
  <div class="home">
    <h1>REAL4PS 项目</h1>
    <div class="buttons">
      <button @click="navigateTo('/problem-orientation')">问题定向</button>
      <button @click="navigateTo('/problem-list')">问题列表</button>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 20px;
}

.buttons {
  margin-top: 20px;
}

button {
  margin: 0 10px;
  padding: 10px 20px;
  font-size: 16px;
}
</style>