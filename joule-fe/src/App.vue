<template lang="jade">
.wrapper
  header.main-header
    a.logo.logo-top(href='index.html')
      span.logo-mini.metalerg-mini
      span.logo-lg.metalerg
    nav.navbar.navbar-static-top(role='navigation')
      a.sidebar-toggle(href='#', data-toggle='offcanvas', role='button')
        span.sr-only Toggle navigation
      .navbar-header.hidden-xs
        span.navbar-brand Joule - {{ generalSettings.name }}
      .navbar-custom-menu
        ul.nav.navbar-nav
          li.dropdown.user.user-menu
            a.dropdown-toggle(href='#', data-toggle='dropdown')
              | Grzegorz Skrzypczak
            ul.dropdown-menu
              li.user-header
                p
                  | Grzegorz Skrzypczak
                  small Administrator
              li.user-footer
                .pull-right
                  a.btn.btn-default.btn-flat(href='#') Sign out
  aside.main-sidebar
    section.sidebar
      ul.sidebar-menu
        li.header MENU
        li(v-link-active)
          a(v-link="{ path: '/parameters', activeClass: 'active'}")
            i.fa.ion-ios-pulse-strong
            span Bieżące parametry
        li(v-link-active)
          a(v-link="{ path: '/temperatures', activeClass: 'active'}")
            i.fa.ion-thermometer
            span Temperatury
        li(v-link-active)
          a(v-link="{ path: '/control', activeClass: 'active'}")
            i.fa.ion-wrench
            span Sterowanie
        li(v-link-active)
          a(v-link="{ path: '/settings', activeClass: 'active'}")
            i.fa.ion-ios-gear
            span Ustawienia
  .content-wrapper
    router-view
  .loading-wrapper(v-show="generalSettings.loading")
    bounce-loader
    p Wczytywanie danych...
  .error-wrapper(v-show="generalSettings.safety_switch")
    i.fa.ion-alert-circled
    p Aplikacja zatrzymana, wyłącznik awaryjny aktywowany!
  .error-wrapper(v-show="generalSettings.error")
    i.fa.ion-bug
    p Aplikacja zatrzymana, błąd modułu sterującego!
    span {{ generalSettings.error_source }}  {{ generalSettings.error_text }}
  footer.main-footer
    strong Copyright © 2016 
    span.synergia-logo
    |  All rights reserved.
</template>

<script>
import store from './vuex/store'
import { generalSettings } from './vuex/getters'
import BounceLoader from 'vue-spinner/src/BounceLoader'
import api from './api/api'

export default {
  components: {
    BounceLoader
  },
  store,
  vuex: {
    getters: {
      generalSettings: generalSettings
    },
    actions: {
    }
  },
  created () {
    // api.mock(this.$store)
    api.initialize(this.$store)
  },
  ready () {
    if (window.innerWidth < 991) {
      document.getElementById('main').classList.add('sidebar-collapse')
    }
    /*eslint-disable */
    window.dispatchEvent(new Event('resize'))
  }
}
</script>

<style lang="sass">
  @import assets/bootstrap/css/bootstrap.min.css
  @import assets/admin-lte/css/font-awesome.min.css
  @import assets/admin-lte/css/ionicons.min.css
  @import assets/admin-lte/css/AdminLTE.min.css
  @import assets/admin-lte/css/skins/skin-red.min.css

  @media (min-width: 767px)
    .metalerg
      background-size: 100%

  .synergia-logo
    background-image: url('assets/synergia.png')
    height: 20px
    background-repeat: no-repeat
    min-width: 90px
    background-size: contain
    display: inline-block
    position: static
    transform: translateY(8px)


  .metalerg
    background-image: url('assets/metalerg.png')
    height: inherit
    background-repeat: no-repeat
    background-position-x: 50%
    background-position-y: 50%

  .metalerg-mini
    background-image: url('assets/metalerg.png')
    float: left
    height: inherit
    width: inherit
    background-repeat: no-repeat
    background-position: 0 50%
    background-size: 210px

  .logo-top
    background-color: #FFFFFF !important

  .navbar-nav>.user-menu>.dropdown-menu>li.user-header
    height: 100%

  .wrapper
    position: inherit

  .main-footer
    position: fixed
    bottom: 0
    width: 100%

  .wrapper
    position: fixed;
    height: 100%;
    width: 100%

  .content-header
    padding: 15px;

  .content
    padding: 0 15px 0 15px;
    height: calc(100% - 160px)
    overflow-y: auto;
    min-height: 10px !important

  @media (max-width: 767px)
    .content
      padding-bottom: 40px

  .info-box-icon
    width: 30px

  .info-box-content
    margin-left: 30px !important

  .loading-wrapper
    position: fixed
    z-index: 2000
    left: 0
    top: 0
    width: 100%
    height: 100%
    background-color: rgb(0,0,0)
    background-color: rgba(0,0,0,0.9)
    color: rgb(255, 255, 255)

    div, p
      position: absolute;
      top: 50%;
      left: 50%;
      margin-right: -50%;
      transform: translate(-50%, -50%)
      font-size: 30px

    p
      padding-top: 50px

  .error-wrapper
    position: fixed
    z-index: 2000
    left: 0
    top: 0
    width: 100%
    height: 100%
    background-color: rgba(221,75,57,1)
    color: rgb(255, 255, 255)

    div, p, i, span
      font-size: 30px
      width: 100%
      display: block;
      word-wrap: break-word;
      margin-left: auto
      margin-right: auto
      text-align: center
    i
      margin-top: 20%;
      font-size: 150px
    p
      line-height: 1
      font-size: 3em
    span
      font-size: 15px
      font-style: italic
      max-height: 10%
      width: 60%
      overflow: auto
      margin-top: 20px
      color: #670C00
</style>
