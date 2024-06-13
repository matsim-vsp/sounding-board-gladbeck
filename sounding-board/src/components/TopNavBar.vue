<template lang="pug">
nav.navbar.is-link(role="navigation" aria-label="main navigation")
  .navbar-brand
    p.navbar-item(:style="{color: 'white'}") Sounding Board - Berlin


  .navbar-end
    img(src="@/assets/images/vsp-logo-white.png" width=300)
        
</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'

@Component({})
export default class VueComponent extends Vue {
  private isBurgerActive = false
  private isDropdownActive = false

  private clickedBurger() {
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

.navbar.is-link {
  background-color: #c40d1e;
  font-weight: 600;
  font-size: 1rem;
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

.navbar-end {
  margin-right: 0.75em;
}

.navbar {
    min-height: 4rem!important;
  }

.navbar,
.navbar-menu,
.navbar-start,
.navbar-end {
  -webkit-box-align: stretch;
  -ms-flex-align: stretch;
  align-items: stretch;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.navbar-end {
  -webkit-box-pack: end;
  -ms-flex-pack: end;
  justify-content: flex-end;
  margin-left: auto;
  display: flex;
  -webkit-box-align: stretch;
  -ms-flex-align: stretch;
  align-items: stretch;
  padding: 10px;
}

@media screen and (max-width: 600px) {
  .navbar.is-link {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
  }

  .navbar-end {
    justify-content: initial;
    margin-left: initial;
  }
}
</style>
