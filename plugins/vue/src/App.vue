<template>
  <div id="app" class="section-profile">
    <div class="">
      <div>
        <h2>Training: {{ selectedCert }}</h2>
      </div>
      <div>
        <h3>Badges: </h3>
        <p v-for="(badge, index) in badgeList" :key="index">{{ badge.name }}</p>
      </div>
      <div v-for="(flag, index) in flagList" :key="index">
        <Flag v-bind:msg="flag.name"></Flag>
        <div>{{ flag.challenge }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import Flag from './components/Flag.vue';
import data from '../tempBadgeData.json';

// const Host = "http://localhost:8888";

export default {
  name: 'App',
  components: {
    Flag
  },
  data: function () {
    return {
      selectedCert: "User Certificate", // TODO make dynamic later
      badgeList: [],
      flagList: []
    }
  },
  methods: {
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
  },
  beforeMount() {
    // this.getTraining();
    this.getFlags(data);
  }
}
</script>

<style></style>
