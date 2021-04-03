<template>
  <div class="border-2 border-caldera-red rounded font-sans">
    <div class="bg-caldera-red lg:text-2xl md:text-lg sm:text-base flex justify-center rounded">
      <p class="text-lg text-colors-white 1">{{ flag.name }}</p>
    </div>
    <div class="flex flex-col justify-center p-2 text-base">
      <div>
        <div><p>{{ flag.challenge }}</p></div>
        <div class="flex justify-center p-2 break-words">
          <button v-if="!showMore" class="w-4 hover:bg-caldera-red rounded" v-on:click="showMore = true">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
            </svg>
          </button>
        </div>
      </div>
      <div class="flex flex-col justify-center" v-if="showMore">
        <p>{{ flag.extra_info }}</p>
        <div class="flex justify-center p-2">
          <a class="hover:underline" target="_blank"
             v-bind:href="`/plugin/training/solution-guides/certificates/${flag.certName}/badges/${flag.badge_name}/flags/${flag.name}`">View
            Solution Guide</a>
        </div>
        <div class="flex justify-center p2">
          <button class="w-4 hover:bg-caldera-red rounded" v-on:click="showMore = false">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Flag',
  data: function () {
    return {showMore: false}
  },
  props: {
    // certName: String,
    flag: Object
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
