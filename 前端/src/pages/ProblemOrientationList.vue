<script setup>
import { ref } from 'vue'

const problems = ref([
  { id: 1, a: '问题1A', b: '问题1B', c: '问题1C', d: '问题1D' },
  { id: 2, a: '问题2A', b: '问题2B', c: '问题2C', d: '问题2D' },
  { id: 3, a: '问题3A', b: '问题3B', c: '问题3C', d: '问题3D' }
])
</script>

<template>
  <div class="list-container">
    <h1>问题列表</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>A</th>
          <th>B</th>
          <th>C</th>
          <th>D</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="problem in problems" :key="problem.id">
          <td>{{ problem.id }}</td>
          <td>{{ problem.a }}</td>
          <td>{{ problem.b }}</td>
          <td>{{ problem.c }}</td>
          <td>{{ problem.d }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.list-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>