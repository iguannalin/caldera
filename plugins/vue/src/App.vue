<template>
  <div class="flex border-caldera-red border-2 rounded-3xl m-5 p-6 text-colors-white font-sans bg-colors-black">
    <div v-if="!selectedCert" class="flex justify-center flex-col w-full">
      <div class="flex justify-center flex-col items-center">
        <h2 class="text-colors-white text-2xl">Choose a certificate:</h2>
        <div class="flex justify-center items-center mt-2">
          <div class="flex flex-col justify-center items-center p-2" v-for="(cert, index) in certificateTypes" :key="index">
            <button v-bind:value="selectedCert" v-on:click="selectedCert = cert">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"/>
              </svg>
              <span class="text-sm">{{ cert }}</span>
            </button>


            <!--            <label v-bind:for="cert" class="text-color-black text-base pl-1 pr-1">-->
            <!--              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">-->
            <!--                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd"/>-->
            <!--              </svg>-->
            <!--              <span>{{ cert }}</span>-->
            <!--            </label>-->
            <!--            <input class="hid" v-bind:id="cert" type="radio" v-model="selectedCert" v-bind:value="cert"/>-->
          </div>
        </div>
      </div>
    </div>
    <div v-else class="flex justify-center flex-col w-full">
      <div class="flex justify-center">
        <h2 class="text-colors-white text-2xl">Training: {{ selectedCert }}</h2>
        <input type="radio" v-bind:value="''" v-model="selectedCert"/><label>Choose different user</label>
      </div>
      <div class="flex justify-center items-center flex-wrap">
        <h3 class="text-lg">Badges: </h3>
        <div class="flex justify-center flex-col" v-for="(badge, index) in badgeList" :key="index">
          <!--TODO get badge icon-->
          <!--<div><img v-bind:src="badge.icon"</div>-->
          <p class="text-base pl-1 pr-1">{{ badge.name }}</p>
        </div>
      </div>
      <div class="mt-2" v-for="(flag, index) in flagList" :key="index">
        <Flag v-bind:msg="flag.name"></Flag>
        <div>{{ flag.challenge }}</div>
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
      selectedCert: "",
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
          this.flagList.push(flag);
        }
      }
    }
  }
}
</script>

<style></style>
