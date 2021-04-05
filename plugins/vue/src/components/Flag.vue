<template>
  <div class="border-2 rounded font-sans" v-bind:class="flag.completed ? 'border-caldera-green' : 'border-caldera-red'">
    <div class="lg:text-2xl md:text-lg sm:text-base flex justify-center p-2 align-center"
         v-bind:class="flag.completed ? 'bg-caldera-green' : 'bg-caldera-red'">
      <p class=" flex w-10/12 text-lg text-colors-white justify-start">{{ flag.name }}</p>
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
                  d="M20.618 5.984A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016zM12 9v2m0 4h.01"/>
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
        <div v-if="flag.code.includes('text-entry')">
          <label v-bind:for="flag.code">Write text here:</label>
          <input v-bind:disabled="flag.completed" class="text-colors-black pl-1 pr-2" v-bind:id="flag.code" placeholder="type here"
                 v-on:input="onTextInput"/>
        </div>
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
  },
  methods: {
    onTextInput: function (e) {
      this.flag.completed = (this.flag.answer && this.flag.answer === e.target.value);
      console.log('text entered', e.target.id, e.target.value, 'bool', this.flag.answer === e.target.value);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
