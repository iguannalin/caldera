<template>
  <div class="bg-black text-2xl text-red-700">
    <p class="font-semibold shadow-md">I'm a flag!</p>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'Flag',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
