<template lang="jade">
  section.content-header
    h1
      | Temperatury
  section.content
    .row
      .col-md-12
        .box.box-primary
          .box-header.with-border
            h3.box-title Temperatura 1
            .box-tools
              mdl-switch(:checked.sync="checked") Live
          .box-body
            div(v-show="!checked")
              vue-datetime.picker(value="Początek")
              vue-datetime.picker(value="Koniec")
              button.btn.btn-default.btn-flat Eksportuj
            vue-chart(:chart-type="LineChart", :columns="columns", :rows="rows", :options="options")

</template>

<script>
export default {
  components: {
    'vue-datetime': require('vue-datetimepicker')
  },
  data () {
    return {
      checked: false,
      columns: [{
        'type': 'number',
        'label': 'Timestamp'
      },
      {
        'type': 'number',
        'label': '*C'
      }],
      rows: [
        [123456, 0],
        [123457, 100],
        [123458, 200]
      ],
      options: {
        hAxis: {
          title: 'Timestamp'
        },
        vAxis: {
          title: 'Temperature',
          minValue: 0,
          maxValue: 1000
        },
        height: 600,
        curveType: 'function'
      }
    }
  }
}
</script>

<style>
  .box-tools {
    right: 60px !important;
  }
  .picker {
    max-width: 100px;
  }
  .box-center {
    position:absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .picker>input {
    text-align: center;
  }
</style>
