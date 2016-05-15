<template lang="jade">
  section.content-header
    h1
      | Sterowanie
  section.content
    .row
      .alert.alert-danger.text-center(v-if="generalSettings.mode == 6")
        | Sterowanie ręczne
      .alert.alert-success.text-center(v-if="generalSettings.mode == 5")
        | Sterowanie automatyczne
      .alert.alert-info.text-center(v-if="generalSettings.mode == 4")
        | Stan spoczynkowy
    .row(v-show="generalSettings.mode == 6")
      .col-lg-3.col-md-6(v-for="output in digitalOutputs")
        .box.box-primary
          .box-header.with-border
            h3.box-title {{output.name}}
            .box-tools
              mdl-switch(:checked="output.value", :id="output.id", @change="setDigitalOutput")
      .col-lg-3.col-md-6(v-for="output in analogOutputs")
        .box.box-primary
          .box-header.with-border
            h3.box-title {{output.name}}
            .box-slider
              mdl-slider(:value="output.value", :id="output.id", @change="setAnalogOutput" min="0" max="100")

</template>

<script>
import { digitalOutputs, analogOutputs, generalSettings } from '../vuex/getters'
import { updateAnalogValue, updateDigitalValue } from '../vuex/actions'

export default {
  vuex: {
    getters: {
      analogOutputs: analogOutputs,
      digitalOutputs: digitalOutputs,
      generalSettings: generalSettings
    },
    actions: {
      setAnalogOutput: updateAnalogValue,
      setDigitalOutput: updateDigitalValue
    }
  },
  data () {
    return {
      amounts: null,
      checked: false
    }
  }
}
</script>

<style scoped>
  .box-slider {
    position: absolute;
    top: 10px;
    right: 5px;
    width: 60%;
  }
</style>
