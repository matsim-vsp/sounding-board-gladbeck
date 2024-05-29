<template lang="pug">
.session-div 
    TopNavBar

    .button.sessionOn-btn(@click="toggleSession(true)" v-if="!this.SessionOn") Neue Sitzung beginnen
    br
    .button.sessionOff-btn(@click="toggleSession(false)" v-if="this.SessionOn") Sitzung beenden
    br
    h1 Läuft eine Sitzung: {{ this.SessionOn }}
    br
    button(@click="getResults()") Ergebnisse des Sitzung
    input.sessionResults(type='number', name='ergebnisse') 

</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'
import TopNavBar from '@/components/TopNavBar.vue'

@Component({ components: { TopNavBar }, props: {} })
export default class VueComponent extends Vue {
  private SessionOn = false

  private apiKey = ''

  getApiAuthorization() {
    let auth = localStorage.getItem('brendan-api-key')
    if (!auth) auth = prompt('API access key required:')

    if (auth) {
      this.apiKey = auth
      localStorage.setItem('brendan-api-key', auth)
    }
  }

  private mounted() {
    this.getApiAuthorization()
  }

  private async toggleSession(sessionStatus: boolean) {
    if (sessionStatus) {
      this.SessionOn = true
      console.log('Session is on')
    } else {
      this.SessionOn = false
    }

    try {
      let response = await fetch('http://127.0.0.1:5000/sessionOn', {
        headers: {
          Authorization: this.apiKey,
          'Content-type': 'text',
          'Access-Control-Allow-Origin': '*',
        },
        method: 'POST',
        body: String(this.SessionOn),
      })

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
      }
      let json = await response.json()
      console.log(json)
    } catch (e) {
      console.log('Error fetching paths :-(')
      return
    }
  }

  private async getResults() {
    var sessionReq = document.querySelector('.sessionResults')
    if (sessionReq) {
      console.log(sessionReq.value)
    } else {
      console.log('Input element not found')
    }

    var reqURL = 'http://127.0.0.1:5000/getVotes/' + sessionReq.value

    try {
      let response = await fetch(reqURL, {
        headers: {
          Authorization: this.apiKey,
        },
        method: 'GET',
      })
      .then((response) => response.json())
      .then((json) => console.log(json));
    } catch (e) {
      console.log('Error fetching paths :-(')
      return
    }
  }
}
</script>

<style>
.session-div {
  min-height: 200px;
  text-align: center;
}

.sessionOn-btn {
  color: white;
  font-size: 16px;
  /* margin: 20px 2px; */
  background-color: #3a76af;
  font-weight: bold;
  margin-top: 50px;
  align-items: center;
  justify-content: center;
}

.sessionOn-btn:hover {
  background-color: white;
  color: #3a76af;
  border: 1px solid #3a76af;
}

.sessionOff-btn {
  color: white;
  font-size: 16px;
  /* margin: 20px 2px; */
  background-color: #af3c3a;
  font-weight: bold;
  margin: 25px 0 50px 0;
  align-items: center;
  justify-content: center;
}

.sessionOff-btn:hover {
  background-color: white;
  color: #af3c3a;
  border: 1px solid #af3c3a;
}

h1 {
  font-size: 24px;
  font-weight: bold;
}
</style>
