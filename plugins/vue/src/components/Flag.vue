<template>
  <div class="border-2 border-caldera-red rounded font-sans">
    <div class="bg-caldera-red lg:text-2xl md:text-lg sm:text-base flex justify-center rounded p-2 align-center">
      <p class="w-10/12 text-lg text-colors-white justify-start">{{ flag.name }}</p>
      <div class="w-2/12 flex justify-end">
        <span v-if="flag.completed" class="w-4 flex align-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
          </svg>
        </span>
        <p v-else class="w-4 flex align-center">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 9  v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
        </p>
      </div>
    </div>
    <div class="flex flex-col justify-center p-2 text-base break-words">
      <div>
        <div>
          <p>{{ flag.challenge }}</p>
        </div>
        <div class="flex justify-center p-2">
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
             v-bind:href="`/plugin/training/solution-guides/certificates/${flag.cert_name}/badges/${flag.badge_name}/flags/${flag.name}`">View
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
    flag: Object
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
