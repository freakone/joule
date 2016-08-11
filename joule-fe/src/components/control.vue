<template lang="jade">
  section.content-header
    h1
      | Sterowanie

    .panic-button(v-if="generalSettings.mode == 6", @click="panicButton(digitalOutputs)")
      | ! OFF !
  section.content
    .row
      .alert.alert-danger.text-center(v-if="generalSettings.mode == 6")
        | Sterowanie ręczne
      .alert.alert-success.text-center(v-if="generalSettings.mode == 5")
        | Sterowanie automatyczne
      .alert.alert-info.text-center(v-if="generalSettings.mode == 4")
        | Stan spoczynkowy
    .row(v-show="generalSettings.mode == 5")
      .alert.alert-warning.text-center(v-if="generalSettings.mode == 5")
        | {{regulatorMode}}
    .row
      .col-sm-6.col-lg-3.col-md-6.col-xs-6(v-for="output in digitalOutputs | filterBy true in 'control'")
        .box.box-primary(@click="setDigitalOutput(output.id, !output.value)", v-bind:class="{'box-active': output.value}")
          .box-button
            .box-button-title {{output.name}}
      .col-sm-6.col-lg-3.col-md-6.col-xs-6(v-for="motor in motors")
        .box.box-warning(@click="updateMotorValue(motor.id, !motor.value)", v-bind:class="{'box-disabled-motor': motor.starting, 'box-active-motor': motor.value}", :disabled="motor.starting")
          .box-button
            .box-button-title {{motor.name}}
      .col-sm-12.col-lg-3.col-md-6.col-xs-6(v-for="output in analogOutputs")
        .box.box-primary
          .box-header.with-border
            h3.box-title {{output.name}}
            .box-slider
              mdl-slider(:value="output.value", :id="output.id", @change="setAnalogOutput" min="0" max="100")

</template>

<script>
import { digitalOutputs, analogOutputs, generalSettings, motors, regulatorMode } from '../vuex/getters'
import { updateAnalogValue, updateDigitalValue, updateMotorValue, panicButton } from '../vuex/actions'

export default {
  vuex: {
    getters: {
      analogOutputs: analogOutputs,
      digitalOutputs: digitalOutputs,
      generalSettings: generalSettings,
      motors: motors,
      regulatorMode: regulatorMode
    },
    actions: {
      setAnalogOutput: updateAnalogValue,
      setDigitalOutput: updateDigitalValue,
      updateMotorValue: updateMotorValue,
      panicButton: panicButton
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

  .panic-button {
    display: flex;
    align-items: center;
    position: absolute;
    right: 0;
    width: 20%;
    background-color: #f39c12;
    justify-content: center;
    padding: 10px;
    margin: 5px;
    border-radius: 3px;
    top: 0;
    bottom: 0;
    font-weight: bold;
    cursor: pointer;
  }

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
  .box-active-motor {
    background-color: #f39c12;
    color: white;
  }
  .box-disabled-motor {
    background-color: #919191;
    color: white;
  }
  @media (max-width: 992px) {
    .box-button {
         height: 20vh;
       }
  }
  @media (max-width: 500px) {
    .box-button {
         height: 10vh;
     }
    .box-button-title {
      font-size: 2em;
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
