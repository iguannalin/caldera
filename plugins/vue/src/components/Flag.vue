<template>
  <div class="bg-caldera-red text-2xl">
    <p class="font-semibold text-colors-white">{{ msg }}</p>
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
</style>
