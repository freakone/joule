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
              label.col-sm-1.control-label
                | Start:
              .col-sm-4
                datetime(v-ref:start-picker, :model.sync="startDatetime", :on-change="onStartDatetimeChanged", type="date")
              label.col-sm-1.control-label
                | Koniec:
              .col-sm-4
                datetime(v-ref:end-picker,:model.sync="endDatetime", :on-change="onEndDatetimeChanged", type="date")
              button.btn.btn-default.btn-flat.col-sm-2 Eksportuj
            .row &nbsp;
            div
              line-chart(:height="100", :responsive="true",:labels="selectedSensor.labels",:datasets="selectedSensor.datasets")

</template>

<script>
import { LineChart } from 'vue-chart.js'
import moment from 'moment'
import { selectTemperature } from '../vuex/actions'
import { temperatureSensors, selectedSensor } from '../vuex/getters'
import Datetime from 'vue-datetime-picker/src/vue-datetime-picker.js'

export default {
  components: {
    Datetime,
    LineChart
  },
  methods: {
    onStartDatetimeChanged: function (newStart) {
      var endPicker = this.$refs.endPicker.control
      endPicker.minDate(newStart)
    },
    onEndDatetimeChanged: function (newEnd) {
      var startPicker = this.$refs.startPicker.control
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
    return {
      liveChecked: true,
      startDatetime: moment().subtract(7, 'days'),
      endDatetime: null
    }
  }
}
</script>

<style>
  .box-tools {
    right: 60px !important;
  }
  .box-center {
    position:absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
</style>
