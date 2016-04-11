<template lang="jade">
  #app
    header.main-header
      a.logo.logo-top(href='index.html')
        span.logo-mini.metalerg-mini
        span.logo-lg.metalerg
      nav.navbar.navbar-static-top(role='navigation')
        a.sidebar-toggle(href='#', data-toggle='offcanvas', role='button')
          span.sr-only Toggle navigation
        .navbar-header.hidden-xs
          span.navbar-brand Joule
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
          li.active
            a(href='#')
              i.fa.ion-ios-pulse-strong
              span Bieżące parametry
           li.active
            a(href='#')
              i.fa.ion-thermometer
              span Temperatury
          li.active
            a(href='#')
              i.fa.ion-wrench
              span Sterowanie
          li.active
            a(href='#')
              i.fa.ion-ios-gear
              span Ustawienia
    .content-wrapper
      section.content-header
        h1
          | Bieżące parametry
      section.content
    footer.main-footer
      .pull-right.hidden-xs
        | Smart boiler control system
      strong Copyright © 2016 Synergia.
      |  All rights reserved.
</template>

<script>
import Hello from './components/Hello'

export default {
  components: {
    Hello
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
</style>
