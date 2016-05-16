<template lang="jade">
  section.content-header
    h1
      | Bieżące parametry
  section.content
    .col-md-8
      .row
        .col-md-6(v-for="temp in temperatureSensors")
          .box.box-primary
            .box-header.with-border
              h3.box-title {{ temp.name }} [{{temp.currentValue}}*C]
            .box-body
               line-chart(:responsive='true', :labels='temp.labels', :datasets='temp.datasets')
      .row
        .col-md-3.col-xs-6(v-for="output in analogOutputs")
          .box.box-primary
            .box-header.with-border
              h3.box-title {{ output.name }}
            .box-body
              knob(:id="output.id", :actual_value="output.actual_value")
    .col-md-2
      .row(v-for="di in digitalInputs")
        .info-box
          span.info-box-icon(:class="{ 'bg-red' : di.value, 'bg-green' : !di.value }")
          .info-box-content
            span.info-box-text {{ di.name }}
     .col-md-2
      .row(v-for="do in digitalOutputs")
        .info-box
          span.info-box-icon(:class="{ 'bg-red' : !do.value, 'bg-green' : do.value }")
          .info-box-content
            span.info-box-text {{ do.name }}


</template>

<script>
import Knob from './knob-vue'
import { LineChart } from 'vue-chart.js'
import { temperatureSensors, digitalOutputs, analogOutputs, digitalInputs } from '../vuex/getters'

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
      digitalInputs: digitalInputs
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
