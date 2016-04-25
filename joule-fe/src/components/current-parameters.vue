<template lang="jade">
  section.content-header
    h1
      | Bieżące parametry
  section.content
    .row
      .col-md-10
        .col-md-6(v-for="temp in temperatureSensors")
          .box.box-primary
            .box-header.with-border
              h3.box-title {{ temp.name }}
            .box-body
              line-chart(:responsive="true",:labels="temp.labels",:datasets="temp.datasets",:options="temp.options")
      .col-md-2
        .row(v-for="do in digitalOutputs")
          .info-box
            span.info-box-icon(:class="{ 'bg-red' : !do.value, 'bg-green' : do.value }")
            .info-box-content
              span.info-box-text {{ do.name }}

    .row
      .col-md-10
        .col-md-2.col-xs-6(v-for="input in analogInputs")
          .box.box-primary
            .box-header.with-border
              h3.box-title {{ input.name }}
            .box-body
              knob(:id="input.id")
</template>

<script>
import Knob from './knob-vue'
import { LineChart } from 'vue-chart.js'
import { analogInputs } from '../vuex/getters'
import { temperatureSensors } from '../vuex/getters'
import { digitalOutputs } from '../vuex/getters'

export default {
  components: {
    Knob,
    LineChart
  },
  vuex: {
    getters: {
      analogInputs: analogInputs,
      temperatureSensors: temperatureSensors,
      digitalOutputs: digitalOutputs
    },
    actions: {
    }
  }
}
</script>

<style scoped>
  .info-box-icon {
    height: 40px;
  }

  .info-box {
    min-height: 40px;
  }

  .info-box-content {
    padding: 10px;
  }
</style>
