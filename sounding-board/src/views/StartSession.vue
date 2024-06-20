<template lang="pug">
.session-div 
  TopNavBar
  <br>
  h1 Läuft eine Sitzung: {{ this.SessionOn }}
  .button.sessionOn-btn(@click="toggleSession(true)" v-if="!this.SessionOn") Neue Sitzung beginnen
  .button.sessionOff-btn(@click="toggleSession(false)" v-if="this.SessionOn") Sitzung beenden

  br
  //- h3 letzte Sitzung: {{ this.mostRecentSession }}
  .button.getSession-btn(@click="getLastSession()") Letzte Sitzung
  <br>
  input.sessionResults(type='number', name='ergebnisse') 
  <br>
  .button.sessionResults-btn(@click="getResults()") Ergebnisse der Sitzung

  .results
    Plotly(:data="data" :layout="plotlyLayout" :options="options" v-if="this.showResults")
  

</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'
import TopNavBar from '@/components/TopNavBar.vue'
// import { Plotly } from 'vue-plotly'
import Plotly from '@/components/VuePlotly.vue'

@Component({ components: { TopNavBar, Plotly }, props: {} })
export default class VueComponent extends Vue {
  private SessionOn = false
  private showResults = false

  private apiKey = ''

  private titleGraphSession = null

  private plotlyLayout = {}

  private data = []

  private options = {responsive: true}

  private conditionTotalVotes = 0

  private serverURL = "https://vsp-lndw-sounding-board.fly.dev/"
  // private serverURL = "http://127.0.0.1:5000/"

  // private mostRecentSession = this.getLastSession()

  private async getLastSession() {
    var reqURL = this.serverURL + 'getLastSession/'
    var lastSession = '0'
    try {
      let response = await fetch(reqURL, {
        headers: {
          Authorization: this.apiKey,
        },
        method: 'GET',
      })
        .then(response => response.text())
        .then(text => (lastSession = text))
    } catch (e) {
      console.log('Error fetching paths :-(')
      prompt("incorrect API access key. Please press OK and try again.")
      this.getApiAuthorization()
      return
    }
    var sessionReq: HTMLInputElement = document.querySelector('.sessionResults')
    sessionReq.value = lastSession
  }

  getApiAuthorization() {
    let auth = localStorage.getItem('api-key2')
    if (!auth) auth = prompt('API access key required:')

    if (auth) {
      this.apiKey = auth
      localStorage.setItem('2api-key2', auth)
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
      let response = await fetch(this.serverURL + 'sessionOn', {
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
      prompt("incorrect API access key. Please press OK and try again.")
      this.getApiAuthorization()
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
    this.titleGraphSession = sessionReq.value

    this.plotlyLayout = {
      yaxis: { padding: 20 },
      title: 'Ergebnisse von Sitzung: ' + this.titleGraphSession,
      barmode: 'stack',
      showlegend: false,
      responsive: true
    }

    var reqURL = `${this.serverURL}getVotes/${sessionReq.value}`
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
      prompt("incorrect API access key. Please press OK and try again.")
      this.getApiAuthorization()
      return
    }

    console.log(sessionVotes)
    var sessionVotesData = this.getCounts(sessionVotes)



    for (const property in sessionVotesData[0]) {
      this.conditionTotalVotes += sessionVotesData[0][property];
    }



    this.visualizeData(sessionVotesData)
  }

  private getCounts(sessionVotes) {
    var countOepnv = sessionVotes.reduce(function (prev, cur) {
      if (prev.hasOwnProperty(cur.oepnv)) prev[cur.oepnv] += 1
      else prev[cur.oepnv] = 1

      return prev
    }, {})

    var countKiezbloecke = sessionVotes.reduce(function (prev, cur) {
      if (prev.hasOwnProperty(cur.kiezBloecke)) prev[cur.kiezBloecke] += 1
      else prev[cur.kiezBloecke] = 1

      return prev
    }, {})

    var countFahrrad = sessionVotes.reduce(function (prev, cur) {
      if (prev.hasOwnProperty(cur.fahrrad)) prev[cur.fahrrad] += 1
      else prev[cur.fahrrad] = 1

      return prev
    }, {})

    var countParkraum = sessionVotes.reduce(function (prev, cur) {
      if (prev.hasOwnProperty(cur.parkraum)) prev[cur.parkraum] += 1
      else prev[cur.parkraum] = 1

      return prev
    }, {})

    var countahrenderAutoVerkehr = sessionVotes.reduce(function (prev, cur) {
      if (prev.hasOwnProperty(cur.fahrenderAutoVerkehr)) prev[cur.fahrenderAutoVerkehr] += 1
      else prev[cur.fahrenderAutoVerkehr] = 1

      return prev
    }, {})

    var countDRT = sessionVotes.reduce(function (prev, cur) {
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
      y: [sessionVotesData[0].base],
      x: ['ÖPNV  '],

      name: 'ÖPNV - base',
      type: 'bar',
      marker: {
        color: "#B3D9FF"
      },
      legendgroup: 'group1',
      hovertemplate:
        "<b>ÖPNV - base</b><br>" +
        "Stimmen " + sessionVotesData[0].base + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[0].base / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Base'
    }

    var trace2_Oepnv = {
      y: [sessionVotesData[0].dekarbonisiert],
      x: ['ÖPNV  '],

      name: 'ÖPNV - dekarbonisiert',
      type: 'bar',
      marker: {
        color: "#3399FF"
      },
      legendgroup: 'group1',
      hovertemplate:
        "<b>ÖPNV - dekarbonisiert</b><br>" +
        "Stimmen " + sessionVotesData[0].dekarbonisiert + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[0].dekarbonisiert / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Dekarbonisiert'
    }

    var trace3_Oepnv = {
      y: [sessionVotesData[0].stark],
      x: ['ÖPNV  '],

      name: 'ÖPNV - stark',
      type: 'bar',
      marker: {
        color: "#00008B"
      },
      legendgroup: 'group1',
      hovertemplate:
        "<b>ÖPNV - stark</b><br>" +
        "Stimmen " + sessionVotesData[0].stark + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[0].stark / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Stark'
    }

    var trace1_Kiezbloecke = {
      y: [sessionVotesData[1].base],
      x: ['Kiezbloecke  '],
      name: 'KiezBlöcke - base',
      type: 'bar',
      marker: {
        color: "#98FB98"
      },
      legendgroup: 'group2',
      hovertemplate:
        "<b>KiezBlöcke - base</b><br>" +
        "Stimmen " + sessionVotesData[1].base + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[1].base / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Base'
    }
    var trace2_Kiezbloecke = {
      y: [sessionVotesData[1]['ganze Stadt']],
      x: ['Kiezbloecke  '],
      name: 'KiezBlöcke - ganze Stadt',
      marker: {
        color: "#006400"
      },
      type: 'bar',
      legendgroup: 'group2',
      hovertemplate:
        "<b>KiezBlöcke - ganze Stadt</b><br>" +
        "Stimmen " + sessionVotesData[1]['ganze Stadt'] + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[1]['ganze Stadt'] / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Ganze Stadt'
    }

    var trace1_Fahrrad = {
      y: [sessionVotesData[2].base],
      x: ['Fahrrad  '],

      name: 'Fahrrad - base',
      type: 'bar',
      marker: {
        color: "#FFA07A"
      },
      legendgroup: 'group3', hovertemplate:
        "<b>Fahrrad - base</b><br>" +
        "Stimmen " + sessionVotesData[2].base + "<br>" +
        "Prozent der Stimmen " + Math.round((sessionVotesData[2].base / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Base'
    }
    var trace2_Fahrrad = {
      y: [sessionVotesData[2].stark],
      x: ['Fahrrad  '],

      name: 'Fahrrad - stark',
      marker: {
        color: "#8B0000"
      },
      type: 'bar',
      legendgroup: 'group3',
      hovertemplate:
        "<b>Fahrrad - stark</b><br>" +
        "Stimmen " + sessionVotesData[2].stark + "<br>" +
        "Prozent der Stimmen " + Math.round((sessionVotesData[2].stark / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Stark'
    }

    var trace1_Parkraum = {
      y: [sessionVotesData[3].base],
      x: ['Parkraum  '],

      name: 'Parkraum - base',
      type: 'bar',
      marker: {
        color: "#E6E6FA"
      },
      legendgroup: 'group4',
      hovertemplate:
        "<b>Parkraum - base</b><br>" +
        "Stimmen " + sessionVotesData[3].base + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[3].base / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Base'
    }
    var trace2_Parkraum = {
      y: [sessionVotesData[3].BesucherFossilTeuer_alleAnderenPreiswert],
      x: ['Parkraum  '],

      name: 'Parkraum - BesucherFossilTeuer_alleAnderenPreiswert',
      type: 'bar',
      marker: {
        color: "#9370DB"
      },
      legendgroup: 'group4',
      hovertemplate:
        "<b>Parkraum - Teuer für Besucher (fossil)</b><br>" +
        "Stimmen " + sessionVotesData[3].BesucherFossilTeuer_alleAnderenPreiswert + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[3].BesucherFossilTeuer_alleAnderenPreiswert / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Teuer für Besucher (fossil)'
    }
    var trace3_Parkraum = {
      y: [sessionVotesData[3].Besucher_teuer_Anwohner_preiswert],
      x: ['Parkraum  '],

      name: 'Parkraum - Besucher_teuer_Anwohner_preiswert',
      type: 'bar',
      marker: {
        color: "#8A2BE2"
      },
      legendgroup: 'group4',
      hovertemplate:
        "<b>Parkraum - Teuer für Besucher</b><br>" +
        "Stimmen " + sessionVotesData[3].Besucher_teuer_Anwohner_preiswert + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[3].Besucher_teuer_Anwohner_preiswert / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Teuer für Besucher'
    }
    var trace4_Parkraum = {
      y: [sessionVotesData[3].Besucher_teuer_Anwohner_teuer],
      x: ['Parkraum  '],

      name: 'Parkraum - Besucher_teuer_Anwohner_teuer',
      type: 'bar',
      marker: {
        color: "#4B0082"
      },
      legendgroup: 'group4',
      hovertemplate:
        "<b>Parkraum - Teuer für Alle</b><br>" +
        "Stimmen " + sessionVotesData[3].Besucher_teuer_Anwohner_teuer + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[3].Besucher_teuer_Anwohner_teuer / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Teuer für Alle'
    }

    var trace1_Autoverkehr = {
      y: [sessionVotesData[4].base],
      x: ['Autoverkehr'],

      name: 'Autoverkehr - base',
      type: 'bar',
      marker: {
        color: "#FFDAB9"
      },
      legendgroup: 'group5',
      hovertemplate:
        "<b>Autoverkehr - base</b><br>" +
        "Stimmen " + sessionVotesData[4].base + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[4].base / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Base'
    }
    var trace2_Autoverkehr = {
      y: [sessionVotesData[4].mautFossil],
      x: ['Autoverkehr'],

      name: 'Autoverkehr - maut Fossil',
      type: 'bar',
      marker: {
        color: "#FFA07A"
      },
      legendgroup: 'group5',
      hovertemplate:
        "<b>Autoverkehr - Maut Für Verbrenner</b><br>" +
        "Stimmen " + sessionVotesData[4].mautFossil + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[4].mautFossil / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Maut Für Verbrenner'
    }
    var trace3_Autoverkehr = {
      y: [sessionVotesData[4].MautFuerAlle],
      x: ['Autoverkehr'],

      name: 'Autoverkehr - Maut Für Alle',
      type: 'bar',
      marker: {
        color: "#FF7F50"
      },
      legendgroup: 'group5',
      hovertemplate:
        "<b>Autoverkehr - Maut Für Alle</b><br>" +
        "Stimmen " + sessionVotesData[4].MautFuerAlle + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[4].MautFuerAlle / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Maut für Alle'
    }

    var trace4_Autoverkehr = {
      y: [sessionVotesData[4].zeroEmissionsZone],
      x: ['Autoverkehr'],

      name: 'Autoverkehr - zero Emissions Zone',
      type: 'bar',
      marker: {
        color: "#FF8C00"
      },
      legendgroup: 'group5',
      hovertemplate:
        "<b>Autoverkehr - zero Emissions Zone</b><br>" +
        "Stimmen " + sessionVotesData[4].zeroEmissionsZone + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[4].zeroEmissionsZone / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Zero Emissions Zone'
    }
    var trace5_Autoverkehr = {
      y: [sessionVotesData[4].zeroEmissionsZonePlusMaut],
      x: ['Autoverkehr'],

      name: 'Autoverkehr - zero Emissions Zone Plus Maut',
      type: 'bar',
      marker: {
        color: "#CC5500"
      },
      legendgroup: 'group5',
      hovertemplate:
        "<b>Autoverkehr - zero Emissions Zone Plus Maut</b><br>" +
        "Stimmen " + sessionVotesData[4].zeroEmissionsZonePlusMaut + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[4].zeroEmissionsZonePlusMaut / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'ZEZ + Maut'
    }
    var trace6_Autoverkehr = {
      y: [sessionVotesData[4].autofrei],
      x: ['Autoverkehr'],

      name: 'Autoverkehr - Autofrei',
      type: 'bar',
      marker: {
        color: "#B7410E"
      },
      legendgroup: 'group5',
      hovertemplate:
        "<b>Autoverkehr - Autofrei</b><br>" +
        "Stimmen " + sessionVotesData[4].autofrei + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[4].autofrei / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Autofrei'
    }

    var trace1_DRT = {
      y: [sessionVotesData[5].base],
      x: ['DRT'],

      name: 'DRT - base',
      type: 'bar',
      marker: {
        color: "#FFFFE0"
      },
      legendgroup: 'group6',
      hovertemplate:
        "<b>DRT - base</b><br>" +
        "Stimmen " + sessionVotesData[5].base + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[5].base / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Base'
    }
    var trace2_DRT = {
      y: [sessionVotesData[5].nurAussenbezirke],
      x: ['DRT'],

      name: 'DRT - nurAussenbezirke',
      marker: {
        color: "#FFD700"
      },
      type: 'bar',
      legendgroup: 'group6',
      hovertemplate:
        "<b>DRT - nurAussenbezirke</b><br>" +
        "Stimmen " + sessionVotesData[5].nurAussenbezirke + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[5].nurAussenbezirke / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Nur Aussenbezirke'
    }
    var trace3_DRT = {
      y: [sessionVotesData[5].ganzeStadt],
      x: ['DRT'],
      name: 'DRT - ganzeStadt',
      marker: {
        color: "#B8860B"
      },
      type: 'bar',
      legendgroup: 'group6',
      hovertemplate:
        "<b>DRT - ganzeStadt</b><br>" +
        "Stimmen " + sessionVotesData[5].ganzeStadt + "<br>" +
        "Prozent der Stimmen " + Math.floor((sessionVotesData[5].ganzeStadt / this.conditionTotalVotes) * 100) + "%" +
        "<extra></extra>",
      text: 'Ganze Stadt'
    }
    // var trace1_Oepnv = {
    //   x: [sessionVotesData[0].base],
    //   y: ['ÖPNV  '],
    //   orientation: 'h',
    //   name: 'ÖPNV - base',
    //   type: 'bar',
    //   marker: {
    //     color: "#B3D9FF"
    //   },
    //   legendgroup: 'group1',
    //   hovertemplate:
    //     "<b>ÖPNV - base</b><br>" +
    //     "Stimmen " + sessionVotesData[0].base + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[0].base / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Base'
    // }

    // var trace2_Oepnv = {
    //   x: [sessionVotesData[0].dekarbonisiert],
    //   y: ['ÖPNV  '],
    //   orientation: 'h',
    //   name: 'ÖPNV - dekarbonisiert',
    //   type: 'bar',
    //   marker: {
    //     color: "#3399FF"
    //   },
    //   legendgroup: 'group1',
    //   hovertemplate:
    //     "<b>ÖPNV - dekarbonisiert</b><br>" +
    //     "Stimmen " + sessionVotesData[0].dekarbonisiert + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[0].dekarbonisiert / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Dekarbonisiert'
    // }

    // var trace3_Oepnv = {
    //   x: [sessionVotesData[0].stark],
    //   y: ['ÖPNV  '],
    //   orientation: 'h',
    //   name: 'ÖPNV - stark',
    //   type: 'bar',
    //   marker: {
    //     color: "#00008B"
    //   },
    //   legendgroup: 'group1',
    //   hovertemplate:
    //     "<b>ÖPNV - stark</b><br>" +
    //     "Stimmen " + sessionVotesData[0].stark + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[0].stark / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Stark'
    // }

    // var trace1_Kiezbloecke = {
    //   x: [sessionVotesData[1].base],
    //   y: ['Kiezbloecke  '],
    //   orientation: 'h',
    //   name: 'KiezBlöcke - base',
    //   type: 'bar',
    //   marker: {
    //     color: "#98FB98"
    //   },
    //   legendgroup: 'group2',
    //   hovertemplate:
    //     "<b>KiezBlöcke - base</b><br>" +
    //     "Stimmen " + sessionVotesData[1].base + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[1].base / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Base'
    // }
    // var trace2_Kiezbloecke = {
    //   x: [sessionVotesData[1]['ganze Stadt']],
    //   y: ['Kiezbloecke  '],
    //   orientation: 'h',
    //   name: 'KiezBlöcke - ganze Stadt',
    //   marker: {
    //     color: "#006400"
    //   },
    //   type: 'bar',
    //   legendgroup: 'group2',
    //   hovertemplate:
    //     "<b>KiezBlöcke - ganze Stadt</b><br>" +
    //     "Stimmen " + sessionVotesData[1]['ganze Stadt'] + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[1]['ganze Stadt'] / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Ganze Stadt'
    // }

    // var trace1_Fahrrad = {
    //   x: [sessionVotesData[2].base],
    //   y: ['Fahrrad  '],
    //   orientation: 'h',
    //   name: 'Fahrrad - base',
    //   type: 'bar',
    //   marker: {
    //     color: "#FFA07A"
    //   },
    //   legendgroup: 'group3', hovertemplate:
    //     "<b>Fahrrad - base</b><br>" +
    //     "Stimmen " + sessionVotesData[2].base + "<br>" +
    //     "Prozent der Stimmen " + Math.round((sessionVotesData[2].base / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Base'
    // }
    // var trace2_Fahrrad = {
    //   x: [sessionVotesData[2].stark],
    //   y: ['Fahrrad  '],
    //   orientation: 'h',
    //   name: 'Fahrrad - stark',
    //   marker: {
    //     color: "#8B0000"
    //   },
    //   type: 'bar',
    //   legendgroup: 'group3',
    //   hovertemplate:
    //     "<b>Fahrrad - stark</b><br>" +
    //     "Stimmen " + sessionVotesData[2].stark + "<br>" +
    //     "Prozent der Stimmen " + Math.round((sessionVotesData[2].stark / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Stark'
    // }

    // var trace1_Parkraum = {
    //   x: [sessionVotesData[3].base],
    //   y: ['Parkraum  '],
    //   orientation: 'h',
    //   name: 'Parkraum - base',
    //   type: 'bar',
    //   marker: {
    //     color: "#E6E6FA"
    //   },
    //   legendgroup: 'group4',
    //   hovertemplate:
    //     "<b>Parkraum - base</b><br>" +
    //     "Stimmen " + sessionVotesData[3].base + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[3].base / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Base'
    // }
    // var trace2_Parkraum = {
    //   x: [sessionVotesData[3].BesucherFossilTeuer_alleAnderenPreiswert],
    //   y: ['Parkraum  '],
    //   orientation: 'h',
    //   name: 'Parkraum - BesucherFossilTeuer_alleAnderenPreiswert',
    //   type: 'bar',
    //   marker: {
    //     color: "#9370DB"
    //   },
    //   legendgroup: 'group4',
    //   hovertemplate:
    //     "<b>Parkraum - Teuer für Besucher (fossil)</b><br>" +
    //     "Stimmen " + sessionVotesData[3].BesucherFossilTeuer_alleAnderenPreiswert + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[3].BesucherFossilTeuer_alleAnderenPreiswert / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Teuer für Besucher (fossil)'
    // }
    // var trace3_Parkraum = {
    //   x: [sessionVotesData[3].Besucher_teuer_Anwohner_preiswert],
    //   y: ['Parkraum  '],
    //   orientation: 'h',
    //   name: 'Parkraum - Besucher_teuer_Anwohner_preiswert',
    //   type: 'bar',
    //   marker: {
    //     color: "#8A2BE2"
    //   },
    //   legendgroup: 'group4',
    //   hovertemplate:
    //     "<b>Parkraum - Teuer für Besucher</b><br>" +
    //     "Stimmen " + sessionVotesData[3].Besucher_teuer_Anwohner_preiswert + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[3].Besucher_teuer_Anwohner_preiswert / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Teuer für Besucher'
    // }
    // var trace4_Parkraum = {
    //   x: [sessionVotesData[3].Besucher_teuer_Anwohner_teuer],
    //   y: ['Parkraum  '],
    //   orientation: 'h',
    //   name: 'Parkraum - Besucher_teuer_Anwohner_teuer',
    //   type: 'bar',
    //   marker: {
    //     color: "#4B0082"
    //   },
    //   legendgroup: 'group4',
    //   hovertemplate:
    //     "<b>Parkraum - Teuer für Alle</b><br>" +
    //     "Stimmen " + sessionVotesData[3].Besucher_teuer_Anwohner_teuer + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[3].Besucher_teuer_Anwohner_teuer / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Teuer für Alle'
    // }

    // var trace1_Autoverkehr = {
    //   x: [sessionVotesData[4].base],
    //   y: ['Autoverkehr'],
    //   orientation: 'h',
    //   name: 'Autoverkehr - base',
    //   type: 'bar',
    //   marker: {
    //     color: "#FFDAB9"
    //   },
    //   legendgroup: 'group5',
    //   hovertemplate:
    //     "<b>Autoverkehr - base</b><br>" +
    //     "Stimmen " + sessionVotesData[4].base + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[4].base / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Base'
    // }
    // var trace2_Autoverkehr = {
    //   x: [sessionVotesData[4].mautFossil],
    //   y: ['Autoverkehr'],
    //   orientation: 'h',
    //   name: 'Autoverkehr - maut Fossil',
    //   type: 'bar',
    //   marker: {
    //     color: "#FFA07A"
    //   },
    //   legendgroup: 'group5',
    //   hovertemplate:
    //     "<b>Autoverkehr - maut Fossil</b><br>" +
    //     "Stimmen " + sessionVotesData[4].mautFossil + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[4].mautFossil / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Maut für Verbrenner'
    // }
    // var trace3_Autoverkehr = {
    //   x: [sessionVotesData[4].MautFuerAlle],
    //   y: ['Autoverkehr'],
    //   orientation: 'h',
    //   name: 'Autoverkehr - maut Für Alle',
    //   type: 'bar',
    //   marker: {
    //     color: "#FF7F50"
    //   },
    //   legendgroup: 'group5',
    //   hovertemplate:
    //     "<b>Autoverkehr - maut Für Alle</b><br>" +
    //     "Stimmen " + sessionVotesData[4].MautFuerAlle + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[4].MautFuerAlle / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Maut für Alle'
    // }

    // var trace4_Autoverkehr = {
    //   x: [sessionVotesData[4].zeroEmissionsZone],
    //   y: ['Autoverkehr'],
    //   orientation: 'h',
    //   name: 'Autoverkehr - zero Emissions Zone',
    //   type: 'bar',
    //   marker: {
    //     color: "#FF8C00"
    //   },
    //   legendgroup: 'group5',
    //   hovertemplate:
    //     "<b>Autoverkehr - zero Emissions Zone</b><br>" +
    //     "Stimmen " + sessionVotesData[4].zeroEmissionsZone + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[4].zeroEmissionsZone / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Zero Emissions Zone'
    // }
    // var trace5_Autoverkehr = {
    //   x: [sessionVotesData[4].zeroEmissionsZonePlusMaut],
    //   y: ['Autoverkehr'],
    //   orientation: 'h',
    //   name: 'Autoverkehr - zero Emissions Zone Plus Maut',
    //   type: 'bar',
    //   marker: {
    //     color: "#CC5500"
    //   },
    //   legendgroup: 'group5',
    //   hovertemplate:
    //     "<b>Autoverkehr - zero Emissions Zone Plus Maut</b><br>" +
    //     "Stimmen " + sessionVotesData[4].zeroEmissionsZonePlusMaut + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[4].zeroEmissionsZonePlusMaut / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'ZEZ + Maut'
    // }
    // var trace6_Autoverkehr = {
    //   x: [sessionVotesData[4].autofrei],
    //   y: ['Autoverkehr'],
    //   orientation: 'h',
    //   name: 'Autoverkehr - Autofrei',
    //   type: 'bar',
    //   marker: {
    //     color: "#B7410E"
    //   },
    //   legendgroup: 'group5',
    //   hovertemplate:
    //     "<b>Autoverkehr - Autofrei</b><br>" +
    //     "Stimmen " + sessionVotesData[4].autofrei + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[4].autofrei / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Autofrei'
    // }

    // var trace1_DRT = {
    //   x: [sessionVotesData[5].base],
    //   y: ['DRT'],
    //   orientation: 'h',
    //   name: 'DRT - base',
    //   type: 'bar',
    //   marker: {
    //     color: "#FFFFE0"
    //   },
    //   legendgroup: 'group6',
    //   hovertemplate:
    //     "<b>DRT - base</b><br>" +
    //     "Stimmen " + sessionVotesData[5].base + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[5].base / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Base'
    // }
    // var trace2_DRT = {
    //   x: [sessionVotesData[5].nurAussenbezirke],
    //   y: ['DRT'],
    //   orientation: 'h',
    //   name: 'DRT - nurAussenbezirke',
    //   marker: {
    //     color: "#FFD700"
    //   },
    //   type: 'bar',
    //   legendgroup: 'group6',
    //   hovertemplate:
    //     "<b>DRT - nurAussenbezirke</b><br>" +
    //     "Stimmen " + sessionVotesData[5].nurAussenbezirke + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[5].nurAussenbezirke / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Nur Aussenbezirke'
    // }
    // var trace3_DRT = {
    //   x: [sessionVotesData[5].ganzeStadt],
    //   y: ['DRT'],
    //   orientation: 'h',
    //   name: 'DRT - ganzeStadt',
    //   marker: {
    //     color: "#B8860B"
    //   },
    //   type: 'bar',
    //   legendgroup: 'group6',
    //   hovertemplate:
    //     "<b>DRT - ganzeStadt</b><br>" +
    //     "Stimmen " + sessionVotesData[5].ganzeStadt + "<br>" +
    //     "Prozent der Stimmen " + Math.floor((sessionVotesData[5].ganzeStadt / this.conditionTotalVotes) * 100) + "%" +
    //     "<extra></extra>",
    //   text: 'Ganze Stadt'
    // }

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
      trace4_Parkraum,
      trace1_Autoverkehr,
      trace2_Autoverkehr,
      trace3_Autoverkehr,
      trace4_Autoverkehr,
      trace5_Autoverkehr,
      trace6_Autoverkehr,
      trace1_DRT,
      trace2_DRT,
      trace3_DRT,
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

.getSession-btn {
  color: white;
  font-size: 16px;
  /* margin: 20px 2px; */
  background-color: #3a76af;
  font-weight: bold;
  margin: 15px 0 15px 0;
  align-items: center;
  justify-content: center;
}

.getSession-btn:hover {
  background-color: white;
  color: #3a76af;
  border: 1px solid #3a76af;
}

.modebar{
      display: none !important;
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
  margin-top: 30px;
  margin-bottom: 25px;
  justify-content: center;
}

.sessionResults-btn:hover {
  background-color: white;
  color: #3a76af;
  border: 1px solid #3a76af;
}

.results {
  max-width: 80%;
  margin: auto auto 50px auto;
}

input[type="number"],
textarea {
  font: 1rem / 1.5 sans-serif;
  display: flex;
  margin: auto;
  box-sizing: border-box;
  padding: 0.5rem 0.75rem;
}
</style>
