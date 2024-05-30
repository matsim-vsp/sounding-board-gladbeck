<template lang="pug">
.session-div 
    TopNavBar
    <br>
    h1 Läuft eine Sitzung: {{ this.SessionOn }}
    .button.sessionOn-btn(@click="toggleSession(true)" v-if="!this.SessionOn") Neue Sitzung beginnen
    .button.sessionOff-btn(@click="toggleSession(false)" v-if="this.SessionOn") Sitzung beenden
   
    br
    input.sessionResults(type='number', name='ergebnisse') 
    <br>
    .button.sessionResults-btn(@click="getResults()") Ergebnisse des Sitzung

    .results
      Plotly(:data="data" :layout="plotlyLayout" :display-mode-bar="false" v-if="this.showResults")
  

</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'
import TopNavBar from '@/components/TopNavBar.vue'
import { Plotly } from 'vue-plotly'

@Component({ components: { TopNavBar, Plotly }, props: {} })
export default class VueComponent extends Vue {
  private SessionOn = false
  private showResults = false

  private apiKey = ''

  private plotlyLayout = {
    title: 'My graph',
    barmode: 'stack',
  }

  private data = []

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
    var sessionReq: HTMLInputElement = document.querySelector('.sessionResults')
    if (sessionReq) {
      console.log(sessionReq.value)
    } else {
      console.log('Input element not found')
    }

    var reqURL = 'http://127.0.0.1:5000/getVotes/' + sessionReq.value
    var sessionVotes = []
    try {
      let response = await fetch(reqURL, {
        headers: {
          Authorization: this.apiKey,
        },
        method: 'GET',
      })
        .then(response => response.json())
        .then(json => (sessionVotes = json))
    } catch (e) {
      console.log('Error fetching paths :-(')
      return
    }

    var sessionVotesData = this.getCounts(sessionVotes)

    this.visualizeData(sessionVotesData)

  }

  private getCounts(sessionVotes) {
    var countOepnv = sessionVotes.reduce(function(prev, cur) {
      if (prev.hasOwnProperty(cur.oepnv)) prev[cur.oepnv] += 1
      else prev[cur.oepnv] = 1

      return prev
    }, {})

    var countKiezbloecke = sessionVotes.reduce(function(prev, cur) {
      if (prev.hasOwnProperty(cur.kiezBloecke)) prev[cur.kiezBloecke] += 1
      else prev[cur.kiezBloecke] = 1

      return prev
    }, {})

    var countFahrrad = sessionVotes.reduce(function(prev, cur) {
      if (prev.hasOwnProperty(cur.fahrrad)) prev[cur.fahrrad] += 1
      else prev[cur.fahrrad] = 1

      return prev
    }, {})

    var countParkraum = sessionVotes.reduce(function(prev, cur) {
      if (prev.hasOwnProperty(cur.parkraum)) prev[cur.parkraum] += 1
      else prev[cur.parkraum] = 1

      return prev
    }, {})

    var countahrenderAutoVerkehr = sessionVotes.reduce(function(prev, cur) {
      if (prev.hasOwnProperty(cur.fahrenderAutoVerkehr)) prev[cur.fahrenderAutoVerkehr] += 1
      else prev[cur.fahrenderAutoVerkehr] = 1

      return prev
    }, {})

    var countDRT = sessionVotes.reduce(function(prev, cur) {
      if (prev.hasOwnProperty(cur.drt)) prev[cur.drt] += 1
      else prev[cur.drt] = 1

      return prev
    }, {})

    var sessionVotesData = [
      countOepnv,
      countKiezbloecke,
      countFahrrad,
      countParkraum,
      countahrenderAutoVerkehr,
      countDRT,
    ]

    return sessionVotesData
  }

  private visualizeData(sessionVotesData) {
    var trace1_Oepnv = {
      x: ['oepnv'],
      y: [sessionVotesData[0].base],
      name: 'Öpnv - base',
      type: 'bar',
      legendgroup: "group1"
    }
    var trace2_Oepnv = {
      x: ['oepnv'],
      y: [sessionVotesData[0].stark],
      name: 'Öpnv - stark',
      type: 'bar',
      legendgroup: "group1"
    }
    var trace3_Oepnv = {
      x: ['oepnv'],
      y: [sessionVotesData[0].dekarbonisiert],
      name: 'Öpnv - dekarbonisiert',
      type: 'bar',
      legendgroup: "group1"
    }

    var trace1_Kiezbloecke = {
      x: ['Kiezbloecke'],
      y: [sessionVotesData[1].base],
      name: 'KiezBlöcke - base',
      type: 'bar',
      legendgroup: "group2"
    }
    var trace2_Kiezbloecke = {
      x: ['Kiezbloecke'],
      y: [sessionVotesData[1]['ganze Stadt']],
      name: 'KiezBlöcke - stark',
      type: 'bar',
      legendgroup: "group2"
    }

    var trace1_Fahrrad = {
      x: ['Fahrrad'],
      y: [sessionVotesData[2].base],
      name: 'Fahrrad - base',
      type: 'bar',
      legendgroup: "group3"
    }
    var trace2_Fahrrad = {
      x: ['Fahrrad'],
      y: [sessionVotesData[2].stark],
      name: 'Fahrrad - stark',
      type: 'bar',
      legendgroup: "group3"
    }

    var trace1_Parkraum = {
      x: ['Parkraum'],
      y: [sessionVotesData[3].base],
      name: 'Parkraum - base',
      type: 'bar',
      legendgroup: "group4"
    }
    var trace2_Parkraum = {
      x: ['Parkraum'],
      y: [sessionVotesData[3].Besucher_teuer_Anwohner_preiswert],
      name: 'Parkraum - Besucher_teuer_Anwohner_preiswert',
      type: 'bar',
      legendgroup: "group4"
    }
    var trace3_Parkraum = {
      x: ['Parkraum'],
      y: [sessionVotesData[3].Besucher_teuer_Anwohner_teuer],
      name: 'Parkraum - Besucher_teuer_Anwohner_teuer',
      type: 'bar',
      legendgroup: "group4"
    }

    var trace1_Autoverkehr = {
      x: ['Autoverkehr'],
      y: [sessionVotesData[4].base],
      name: 'Autoverkehr - base',
      type: 'bar',
      legendgroup: "group5"
    }
    var trace2_Autoverkehr = {
      x: ['Autoverkehr'],
      y: [sessionVotesData[4].mautFossil],
      name: 'Autoverkehr - maut Fossil',
      type: 'bar',
      legendgroup: "group5"
    }
    var trace3_Autoverkehr = {
      x: ['Autoverkehr'],
      y: [sessionVotesData[4].MautFuerAlle],
      name: 'Autoverkehr - maut Für Alle',
      type: 'bar',
      legendgroup: "group5"
    }

    var trace4_Autoverkehr = {
      x: ['Autoverkehr'],
      y: [sessionVotesData[4].zeroEmissionsZone],
      name: 'Autoverkehr - zero Emissions Zone',
      type: 'bar',
      legendgroup: "group5"
    }
    var trace5_Autoverkehr = {
      x: ['Autoverkehr'],
      y: [sessionVotesData[4].zeroEmissionsZonePlusMaut],
      name: 'Autoverkehr - zero Emissions Zone Plus Maut',
      type: 'bar',
      legendgroup: "group5"
    }
    var trace6_Autoverkehr = {
      x: ['Autoverkehr'],
      y: [sessionVotesData[4].autofrei],
      name: 'Autoverkehr - Autofrei',
      type: 'bar',
      legendgroup: "group5"
    }

    var trace1_DRT = {
      x: ['DRT'],
      y: [sessionVotesData[5].base],
      name: 'DRT - base',
      type: 'bar',
      legendgroup: "group6"
    }
    var trace2_DRT = {
      x: ['DRT'],
      y: [sessionVotesData[5].nurAussenbezirke],
      name: 'DRT - stark',
      type: 'bar',
      legendgroup: "group6"
    }
    var trace3_DRT = {
      x: ['DRT'],
      y: [sessionVotesData[5].ganzeStadt],
      name: 'DRT - stark',
      type: 'bar',
      legendgroup: "group6"
    }

    this.data = [
      trace1_Oepnv,
      trace2_Oepnv,
      trace3_Oepnv,
      trace1_Kiezbloecke,
      trace2_Kiezbloecke,
      trace1_Fahrrad,
      trace2_Fahrrad,
      trace1_Parkraum,
      trace2_Parkraum,
      trace3_Parkraum,
      trace1_Autoverkehr,
      trace2_Autoverkehr,
      trace3_Autoverkehr,
      trace4_Autoverkehr,
      trace5_Autoverkehr,
      trace6_Autoverkehr,
      trace1_DRT,
      trace2_DRT,
      trace3_DRT
    ]

    this.showResults = true
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
  margin: 15px 0 50px 0;
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
  margin: 15px 0 50px 0;
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

.sessionResults-btn {
  color: white;
  font-size: 16px;
  /* margin: 20px 2px; */
  background-color: #3a76af;
  font-weight: bold;
  align-items: center;
  margin-top: 15px;
  margin-bottom: 25px;
  justify-content: center;
}

.sessionResults-btn:hover {
  background-color: white;
  color: #3a76af;
  border: 1px solid #3a76af;
}
</style>
