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
      .col-sm-6.col-lg-3.col-md-6(v-for="output in digitalOutputs | filterBy true in 'control'")
        .box.box-primary(@click="setDigitalOutput(output.id, !output.value)", v-bind:class="{'box-active': output.value}")
          .box-button
            .box-button-title {{output.name}}
      .col-sm-12.col-lg-3.col-md-6(v-for="output in analogOutputs")
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
  .box-button-title {
    display: inline-block;
    font-size: 4em;
    margin: 0;
    line-height: 1;
    text-align: center;
    width: 100%;
  }
  .box-active {
    background-color: #3c8dbc;
    color: white;
  }
  @media (max-width: 992px) {
      .box-button {
         height: 20vh;
       }
  }
  .box-button {
    padding: 10px;
    position: relative;
    display: table-cell;
    vertical-align: middle;
    width: 100vh;
    border: 1px;
    cursor: pointer;
    font-size: 50%;
  }
  .box-slider {
    position: absolute;
    top: 10px;
    right: 5px;
    width: 60%;
  }
</style>
