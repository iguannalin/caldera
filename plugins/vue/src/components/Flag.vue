<template>
  <div>
    <div class="bg-caldera-red text-2xl flex justify-center">
      <p class="font-semibold text-colors-white">{{ flag.name }}</p>
    </div>
    <div>
      <p>{{ flag.challenge }}</p>
      <p>{{ flag.extra_info }}</p>
      <button v-on:click="openFlagSolutionGuide">View Solution Guide</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Flag',
  props: {
    // certName: String,
    flag: Object
  },
  methods: {
    openFlagSolutionGuide: function () {
      console.log('cert?')
      console.log('cert?', this.props.flag.certName)
      window.open(
          `/plugin/training/solution-guides/certificates/${this.props.flag.certName}/badges/${this.props.flag.badge_name}/flags/${this.props.flag.name}`,
          '_blank',
      );
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
