<template lang="jade">
  section.content-header
    h1
      | Bieżące parametry
  section.content
    .row(v-show="generalSettings.mode == 5")
      .alert.alert-warning.text-center(v-if="generalSettings.mode == 5")
        | {{regulatorMode}}
    .row
      .col-md-8
        .row
          .col-md-6(v-for="temp in temperatureSensors")
            .box.box-primary
              .box-header.with-border
                h3.box-title {{ temp.name }} [{{temp.currentValue}}*C]
              .box-body
                 line-chart(:responsive='true', :labels='temp.labels', :datasets='temp.datasets')
        .row
          .col-md-3.col-xs-4(v-for="output in analogOutputs")
            .box.box-primary
              .box-header.with-border
                h3.box-title {{ output.name }}
              .box-body
                knob(:id="output.id", :actual_value="output.actual_value")
      .com-md-4
        .col-md-2.col-xs-6(v-for="di in digitalInputs")
          .info-box
            span.info-box-icon(:class="{ 'bg-red' : di.value, 'bg-green' : !di.value }")
            .info-box-content
              span.info-box-text {{ di.name }}
        .col-md-2.col-xs-6(v-for="do in digitalOutputs")
          .info-box
            span.info-box-icon(:class="{ 'bg-red' : !do.value, 'bg-green' : do.value }")
            .info-box-content
              span.info-box-text {{ do.name }}
        .col-md-2.col-xs-6(v-for="mo in motors")
          .info-box
            span.info-box-icon(:class="{'bg-yellow': mo.starting, 'bg-red' : !mo.value, 'bg-green' : mo.value }")
            .info-box-content
              span.info-box-text {{ mo.name }}


</template>

<script>
import Knob from './knob-vue'
import { LineChart } from 'vue-chart.js'
import { temperatureSensors, digitalOutputs, analogOutputs, digitalInputs, motors, generalSettings, regulatorMode } from '../vuex/getters'

export default {
  components: {
    Knob,
    LineChart
  },
  vuex: {
    getters: {
      analogOutputs: analogOutputs,
      temperatureSensors: temperatureSensors,
      digitalOutputs: digitalOutputs,
      digitalInputs: digitalInputs,
      motors: motors,
      generalSettings: generalSettings,
      regulatorMode: regulatorMode
    },
    actions: {
    }
  }
}
</script>

<style scoped>
  .info-box-icon {
    height: 20px;
  }

  .info-box {
    min-height: 20px;
    margin-bottom: 5px;
  }

  .info-box-content {
    padding: 0px 10px;
  }
</style>
