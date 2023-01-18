<template lang="pug">
nav.navbar.is-link(role="navigation" aria-label="main navigation")
    .navbar-brand
      router-link.home-link.navbar-item(to="/" :style="{color: 'white'}") Home
        //- img(src="https://bulma.io/images/bulma-logo.png" width="112" height="28")

      a.navbar-burger.burger(
        @click='clickedBurger'
        :class="{'is-active': isBurgerActive}"
        role="button"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample")
        span(aria-hidden="true")
        span(aria-hidden="true")
        span(aria-hidden="true")

    #navbarBasicExample.navbar-menu(
      :class="{'is-active': isBurgerActive}"
      @click='clickedBurger'
    )

      .navbar-start

        .navbar-item.has-dropdown.is-hoverable(:class="{'is-active': isDropdownActive}")
          a.navbar-link  Visualizations
          .navbar-dropdown
            a.navbar-item(:href="'/v3?day=5'") Infection Traces
            a.navbar-item(:href="'/timelapse'") 90 Day Time Lapse

        .navbar-item.has-dropdown.is-hoverable(:class="{'is-active': isDropdownActive}")
          a.navbar-link  Mobility
          .navbar-dropdown
            a.navbar-item(:href="'/mobility'") Mobility State
            a.navbar-item(:href="'/mobility-counties/'") Mobility County

        .navbar-item.has-dropdown.is-hoverable(:class="{'is-active': isDropdownActive}")
          a.navbar-link(:href="'/calculators'")  Calculators
          .navbar-dropdown
            a.navbar-item(:href="'/r-calcs/2021-01-24'") R-Calculator (24.Jan)
            a.navbar-item(:href="'/r-calcs/2020-11-14-lockdown59'") R-Calculator (14.Nov, restrictive)
            a.navbar-item(:href="'/r-calcs/2020-11-14-lockdown84'") R-Calculator (14.Nov, permissive)
            a.navbar-item(:href="'/r-calcs/2020-10-23'") R-Calculator (23.Oct)
            hr
            a.navbar-item(:href="'/risk-calcs/2020-11-11'") Activity Risk Calculator

      .navbar-end
        router-link.navbar-item(to="/" :style="{color: 'white'}") About

</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'

@Component({})
export default class VueComponent extends Vue {
  private isBurgerActive = false
  private isDropdownActive = false

  private clickedBurger() {
    console.log('clicked!')
    this.isBurgerActive = !this.isBurgerActive
  }

  @Watch('$route') private async routeChanged(to: any, from: any) {
    //console.log(this.$route)
    this.isBurgerActive = false
    this.isDropdownActive = false
  }
}
</script>

<style scoped lang="scss">
@import '@/styles.scss';

#nav {
  background-color: $matsimBlue;
}

#nav a.router-link-exact-active {
  font-weight: bold;
  color: green;
}

.home-link {
  margin-left: 2.25rem;
}

.navbar-dropdown hr {
  margin: 0.25rem 0;
}

.navbar-dropdown .navbar-item {
  font-size: 0.85rem;
}

@media only screen and (max-width: 640px) {
  .home-link {
    margin-left: 0.25rem;
  }

  .space {
    margin: 0 0.6rem;
  }
}
</style>
