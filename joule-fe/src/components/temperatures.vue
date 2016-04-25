<template lang="jade">
  section.content-header
    h1
      | Temperatury
  section.content
    .row
      .col-md-12
        .box.box-primary
          .box-header.with-border
            h3.box-title
              select.form-control(v-model="temperatureSelectionId" v-on:change="selectTemperature(temperatureSelectionId)")
                option(v-for="temp in temperatureSensors", :value="temp.id")
                  | {{ temp.name }}
            .box-tools
              mdl-switch(:checked.sync="liveChecked") Live
          .box-body
            div(v-show="!checked")
              datetime.picker(value="Początek")
              datetime.picker(value="Koniec")
              button.btn.btn-default.btn-flat Eksportuj
            .row &nbsp;
            .div
            line-chart(:responsive="true",:labels="selectedSensor.labels",:datasets="selectedSensor.datasets",:options="selectedSensor.options")

</template>

<script>
import { LineChart } from 'vue-chart.js'
import Datetime from 'vue-datetimepicker'

import { selectTemperature } from '../vuex/actions'
import { temperatureSensors, selectedSensor } from '../vuex/getters'

export default {
  components: {
    Datetime,
    LineChart
  },
  vuex: {
    getters: {
      temperatureSensors: temperatureSensors,
      selectedSensor: selectedSensor
    },
    actions: {
      selectTemperature
    }
  },
  data () {
    return {
      temperatureSelectionId: 1,
      liveChecked: false
    }
  },
  ready () {

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
