<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  a: '',
  b: '',
  c: '',
  d: ''
})

const submitForm = () => {
  // 这里添加提交逻辑
  router.push('/problem-list')
}
</script>

<template>
  <div class="form-container">
    <h1>问题定向</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="a">A</label>
        <input type="text" id="a" v-model="form.a">
      </div>
      <div class="form-group">
        <label for="b">B</label>
        <input type="text" id="b" v-model="form.b">
      </div>
      <div class="form-group">
        <label for="c">C</label>
        <input type="text" id="c" v-model="form.c">
      </div>
      <div class="form-group">
        <label for="d">D</label>
        <input type="text" id="d" v-model="form.d">
      </div>
      <button type="submit">提交</button>
    </form>
  </div>
</template>

<style scoped>
.form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>