<template>
  <div
      class="flex border-caldera-red border-2 rounded-3xl m-5 p-6 text-colors-white font-sans bg-caldera-grayish">
    <div v-if="!selectedCert" class="flex justify-center flex-col w-full">
      <div class="flex justify-center flex-col items-center">
        <h2 class="text-colors-white text-caldera-reddish text-2xl">Choose a certificate:</h2>
        <div class="flex justify-center items-center mt-2">
          <div class="flex flex-col justify-center items-center p-2" v-for="(cert, index) in certificateTypes"
               :key="index">
            <button class="w-24 hover:bg-caldera-red rounded" v-bind:value="selectedCert"
                    v-on:click="selectedCert = cert">
              <!--              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">-->
              <!--                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"/>-->
              <!--              </svg>-->
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span class="text-sm">{{ cert }}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="flex justify-center flex-col w-full">
      <div>
        <div class="flex justify-between mt-2">
          <div class="flex flex-row items-center">
            <h2 class="text-colors-white text-2xl">Training: {{ selectedCert }}</h2>
            <div class="flex pl-5 pr-5">
              <button class="flex flex-col sm:flex-row items-center justify-center hover:bg-caldera-red rounded"
                      v-bind:value="selectedCert"
                      v-on:click="selectedCert = ''">
                <span class="w-8 sm:p-1">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                </span>
                <span class="text-xs sm:p-1">Choose different user</span>
              </button>
            </div>
          </div>
          <div class="flex flex-row justify-between">
            <button class="w-6 hover:bg-caldera-red rounded">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6"/>
              </svg>
            </button>
            <button class="w-6 hover:bg-caldera-red rounded pl-1">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </button>
            <button class="w-6 hover:bg-caldera-red rounded pl-1">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div class="flex justify-center items-center flex-wrap text-caldera-brown">
        <h3 class="text-lg">Badges: </h3>
        <div class="flex justify-center flex-col" v-for="(badge, index) in badgeList" :key="index">
          <!--TODO get badge icon-->
          <!--<div><img v-bind:src="badge.icon"</div>-->
          <p class="text-base pl-1 pr-1">{{ badge.name }}</p>
        </div>
      </div>
      <div class="flex mt-1 justify-between flex-row flex-wrap">
        <div class="lg:w-3/12 md:w-4/12 sm:w-full p-2 box-border" v-for="(flag, index) in flagList" :key="index">
          <Flag :flag="flag"></Flag>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Flag from './components/Flag.vue';
import data from '../tempBadgeData.json';

export default {
  name: 'App',
  components: {
    Flag
  },
  data: function () {
    return {
      selectedCert: '',
      badgeList: [],
      flagList: [],
      certificateTypes: ["User Certificate", "Blue Certificate"]
    }
  },
  watch: {
    selectedCert: function () {
      if (this.selectedCert) {
        console.log('SELECTED', this.selectedCert);
        if (!this.getTraining()) this.getFlags(data);
      } else this.resetData();
    }
  },
  methods: {
    resetData: function () {
      this.badgeList = [];
      this.flagList = [];
    },
    getTraining: function () {
      fetch('/plugin/training/flags', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name: this.selectedCert, answers: {}}),
      }).then(r => {
        if (r.ok) return r.json(); else console.error('Fetch error:', r)
      }).then((data) => {
        console.log('success', data);
        this.getFlags(data);
        return true;
      }).catch(e => console.error(e));
    },
    getFlags: function (data) {
      for (const badgeIndex in data.badges) {
        const badge = data.badges[badgeIndex];
        console.log('BADGE', badge);
        this.badgeList.push(badge);
        for (const flagIndex in badge.flags) {
          const flag = badge.flags[flagIndex]
          this.flagList.push({...flag, badge_name: badge.name, certName: this.selectedCert});
        }
      }
    }
  }
}
</script>

<style></style>
