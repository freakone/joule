<template lang="jade">
  section.content-header
    h1
      | Ustawienia
  section.content
    .row
      .col-md-6
        .box.box-primary
          .box-header.with-border
            h3.box-title Ogólne
          .box-body
            input.form-control(type="text" placeholder="Nazwa kotła")
      .col-md-6
        .box.box-primary
          .box-header.with-border
            h3.box-title Nazwy peryferiów
          .box-body
            .row(v-for="item in ['1', '2', '3']")
              .col-xs-2
                | Wyjście {{item}}
              .col-xs-10
                input.form-control(type="text" placeholder="Wyjście {{item}}")
            .row(v-for="item in ['1', '2', '3']")
              .col-xs-2
                | Wejście {{item}}
              .col-xs-10
                input.form-control(type="text" placeholder="Wejście {{item}}")

    .row
      .col-md-3(v-for="item in ['1', '2', '3', '4']")
        .box.box-primary
          .box-header.with-border
            h3.box-title Czujnik temperatury {{item}} [20*C]
          .box-body
            .row
              .col-xs-12
                input.form-control(type="text" placeholder="Nazwa czujnika")
            .row
              | &nbsp;
            .row
                .col-xs-2
                  | Minimum
                .col-xs-6
                  mdl-slider(:value.sync="amount_min_1" min="0" max="100")
                .col-xs-4
                  input.form-control(type="text", placeholder="Wartosc", :value="amount_min_1")
            .row
                .col-xs-2
                  | Maximum
                .col-xs-6
                  mdl-slider(:value.sync="amount" min="0" max="100")
                .col-xs-4
                  input.form-control(type="text", placeholder="Wartosc", :value="amount")
</template>

<script>
</script>

<style scoped>
</style>
