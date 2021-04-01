<template>
  <div id="app" class="section-profile">
    <div id="vueapp-sidebar">
      <button type="button" class="button-success atomic-button" onclick="vueappFunction()">Click me!</button>
    </div>
    <Flag msg="This is parent speaking"/>
  </div>
</template>

<script>
import Flag from './components/Flag.vue'

export default {
  name: 'App',
  components: {
    Flag
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
