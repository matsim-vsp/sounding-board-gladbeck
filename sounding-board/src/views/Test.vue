<template lang="pug">
.session-div 
    TopNavBar

    .button.sessionOn-btn(@click="toggleSession(true)") Neue Sitzung beginnen
    br
    .button.sessionOff-btn(@click="toggleSession(false)") Sitzung beenden

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
      try {
        // this.myState.statusMessage = ''
        let response = await fetch('http://127.0.0.1:5000/sessionOn', {
          headers: {
            Authorization: this.apiKey,
            'Content-type': 'text',
            'Access-Control-Allow-Origin': '*',
          },
          method: 'POST',
          body: 'value: ' + this.SessionOn,
        })

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`)
        }
        let json = await response.json()
        console.log(json)
      } catch (e) {
        // this.myState.statusMessage = 'Error fetching paths :-('
        // this.isFiltering = false
        console.log('Error fetching paths :-(')
        return
      }
    } else {
      console.log('Session is off')
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
</style>
