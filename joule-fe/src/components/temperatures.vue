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
              select.form-control(:value="selectedSensor.id", @change="selectTemperature")
                option(v-for="temp in temperatureSensors", :value="temp.id")
                  | {{ temp.name }}
            .box-tools
              mdl-switch(:checked.sync="liveChecked") Live
          .box-body
            div.form-group(v-show="!liveChecked")
              label.col-sm-1.control-label(for="start-picker")
                | Start:
              .col-sm-4
                vue-datetime-picker(v-ref:start-picker, model="{{@ startDatetime }}", :on-change="onStartDatetimeChanged")
              label.col-sm-1.control-label(for="end-picker")
                | Koniec:
              .col-sm-4
                vue-datetime-picker(v-ref:end-picker, model="{{@ endDatetime }}")
              button.btn.btn-default.btn-flat.col-sm-2 Eksportuj
            .row &nbsp;
            div
              line-chart(:responsive="true",:labels="selectedSensor.labels",:datasets="selectedSensor.datasets",:options="selectedSensor.options")

</template>

<script>
import { LineChart } from 'vue-chart.js'

import { selectTemperature } from '../vuex/actions'
import { temperatureSensors, selectedSensor } from '../vuex/getters'

export default {
  inherit: true,
  components: {
    'vue-datetime-picker': require('vue-datetime-picker/src/vue-datetime-picker.js'),
    LineChart
  },
  methods: {
    onStartDatetimeChanged: function (newStart) {
      console.log('asd')
      var endPicker = this.$ref.endPicker.control
      endPicker.minDate(newStart)
    },
    onEndDatetimeChanged: function (newEnd) {
      var startPicker = this.$.startPicker.control
      startPicker.maxDate(newEnd)
    }
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
    var moment = require('moment')
    return {
      liveChecked: false,
      startDatetime: moment(),
      endDatetime: null
    }
  },
  created () {
    // selectTemperature(1)
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
