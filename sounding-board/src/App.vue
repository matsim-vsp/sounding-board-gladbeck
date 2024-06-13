<template lang="pug">
#app(:class="{'full-screen-app' : state.isFullScreen }")
  //- top-nav-bar#nav(:style="{paddingLeft: state.isFullScreen ? '0rem':''}" )

  .center-area
    router-view.main-view

  .footer(v-if="!state.isFullScreen")
    a(href="https://tu.berlin")
      img(alt="TU-Berlin logo" src="@/assets/images/tu-logo.jpg" width=180)
    a(href="https://vsp.berlin")
      img(alt="VSP TU-Berlin logo" src="@/assets/images/vsp-logo.png" width=100)
    a(href="https://matsim.org")
      img(alt="MATSim logo" src="@/assets/images/matsim-logo-blue.png" width=200)

    p: b Sounding Board <br/>&copy; 2023 VSP TU-Berlin
    p Diese Seite sammelt, speichert oder analysiert keine persönlichen Daten.
      |<br/> Weitere Informationen über VSP an der TU Berlin finden Sie auf unserer Website unter
      a(href="https://vsp.berlin") &nbsp;vsp.berlin

    p
      a(href="https://vsp.berlin/impressum/" target="_blank") Impressum
      a(href="https://vsp.tu-berlin.de/privacy" target="_blank") Datenschutz

</template>

<i18n>
  de:
    dataInformation1: 'Diese Seite sammelt, speichert oder analysiert keine persönlichen Daten.'
    dataInformation2: 'Weitere Informationen über VSP an der TU Berlin finden Sie auf unserer Website unter'
    imprint: 'Imprint'
    privacy: 'Privacy'
  en:
    dataInformation1: 'This site does not collect, store, or analyze any personal information.'
    dataInformation2: 'For more info about VSP at TU Berlin, see our website at'
    imprint: 'Impressum'
    privacy: 'Datenschutz'
  </i18n>

<script lang="ts">
import TopNavBar from '@/components/TopNavBar.vue'
import store from '@/store'

export default {
  name: 'App',
  components: { TopNavBar },
  data: function() {
    return {
      state: store.state,
    }
  },
}
</script>

<style lang="scss">
@import '@/styles.scss';
@import '~bulma/css/bulma.css';

*,
*::before,
*::after {
  box-sizing: inherit;
}

body,
html {
  margin: 0px 0px;
  padding: 0px 0px;
  height: 100%;
  overscroll-behavior: contain;
  background-color: white;
}

canvas {
  display: block;
}

html {
  overflow-y: auto;
  box-sizing: border-box;
}

.full-screen-app {
  height: 100%;
}

.bury-me {
  z-index: -5;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
}

h2 {
  font-size: 2.5rem;
  font-weight: bold;
}

h3 {
  font-size: 1.5rem;
  font-weight: bold;
}

#app {
  // display: grid;
  // grid-template-columns: 1fr;
  // grid-template-rows: auto 1fr auto;
  background-color: $paleBackground;
  color: #222;
  margin: 0rem 0rem;
  padding: 0px 0px;
  font-family: Roboto, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: auto;
  display: flex;
  flex-direction: column;
}

.modebar-group {
  top: -1.2rem;
  right: -1rem;
}

#nav {
  z-index: 5;
  position: sticky;
  top: 0;
  grid-column: 1 / 2;
  grid-row: 1 / 2;
  box-shadow: 0px 2px 10px #00000060;
  height: min-content;
}

.center-area {
  grid-column: 1 / 2;
  grid-row: 2 / 3;
  z-index: 1;
  display: flex;
  flex-direction: column;
  flex: 1;
  //max-height: 100%;
  height: min-content;
}

.main-view {
  flex: 1;
}

#nav a.router-link-exact-active {
  color: #ffffff;
}

.space {
  margin: 0 1rem;
}

#app .footer {
  grid-column: 1 / 2;
  grid-row: 5 / 6;
  padding: 2rem 0.5rem 3rem 2rem;
  background-color: white;
}

.footer p {
  line-height: 1.2rem;
  margin-top: 0.5rem;
  // color: white;
}

.footer a {
  // color: #17a5ec;
  margin-right: 2rem;
}

.footer img {
  margin: 1rem auto;
}

.vue-slider-rail {
  background-color: green;
}
</style>
