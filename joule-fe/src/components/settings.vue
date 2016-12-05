<template lang="jade">
  section.content-header
    h1
      | Ustawienia
  section.content
    .col-md-6
      .row
        .box.box-primary
          .box-header.with-border
            h3.box-title Ogólne
          .box-body
            input.form-control(type="text", placeholder="Nazwa kotła", :value="generalSettings.name", @change="updateName")
      .row
        .col-md-6(v-for="item in temperatureSensors")
          .box.box-primary
            .box-header.with-border
              h3.box-title Czujnik temperatury {{$index+1}} [{{item.currentValue}}*C]
            .box-body
              .row
                .col-xs-12
                   input.form-control(type="text", :value="item.name", :id="item.id" @change="updateTemperatureSensorName")
              .row
                | &nbsp;
              .row
                  .col-xs-4
                    | Minimum
                  .col-xs-4
                    input.form-control(type="number", :value="item.limitMin", :id="item.id", @change.prevent="temperatureMinimum($event, item)")
                  .col-xs-2
                    button(style="width:100%;", @click="minimumIncrement(item)") +10
                  .col-xs-2
                    button(style="width:100%;", @click="minimumDecrement(item)") -10
              .row
                  .col-xs-4
                    | Maximum
                  .col-xs-4
                    input.form-control(type="number", :value="item.limitMax", :id="item.id", @change="temperatureMaximum($event, item)")
                  .col-xs-2
                    button(style="width:100%;", @click="maximumIncrement(item)") +10
                  .col-xs-2
                    button(style="width:100%;", @click="maximumDecrement(item)") -10
    .col-md-6
      .box.box-primary
        .box-header.with-border
          h3.box-title Nazwy peryferiów
        .box-body
          .row(v-for="output in digitalOutputs")
            .col-xs-3
              | Wyjście cyfrowe {{$index+1}}
            .col-xs-9
              input.form-control(type="text", :value="output.name", :id="output.id", @change="updateDigitalOutputName")
          .row(v-for="output in analogOutputs")
            .col-xs-3
              | Wyjście analogowe {{$index+1}}
            .col-xs-9
              input.form-control(type="text", :value="output.name", :id="output.id", @change="updateAnalogOutputName")
          .row(v-for="motor in motors")
            .col-xs-3
              | Silnik {{$index+1}}
            .col-xs-9
              input.form-control(type="text", :value="motor.name", :id="motor.id", @change="updateMotorName")
    </template>

<script>
import { digitalOutputs, analogOutputs, temperatureSensors, generalSettings, motors } from '../vuex/getters'
import { updateName, updateAnalogOutputName, updateDigitalOutputName, updateTemperatureMaximum, updateTemperatureMinimum, updateTemperatureSensorName, updateMotorName } from '../vuex/actions'

export default {
  vuex: {
    getters: {
      analogOutputs: analogOutputs,
      digitalOutputs: digitalOutputs,
      temperatureSensors: temperatureSensors,
      generalSettings: generalSettings,
      motors: motors
    },
    actions: {
      updateName,
      updateAnalogOutputName,
      updateDigitalOutputName,
      updateTemperatureMaximum,
      updateTemperatureSensorName,
      updateTemperatureMinimum,
      updateMotorName
    }
  },
  methods: {
    temperatureMinimum: function (input, item) {
      if (input.target.valueAsNumber < 0 || input.target.valueAsNumber > item.maximumValue) {
        input.target.valueAsNumber = item.limitMin
        return
      }
      updateTemperatureMinimum(this.$store, input)
    },
    temperatureMaximum: function (input, item) {
      if (input.target.valueAsNumber < 0 || input.target.valueAsNumber > item.maximumValue) {
        input.target.valueAsNumber = item.limitMax
        return
      }
      updateTemperatureMaximum(this.$store, input)
    },
    minimumIncrement: function (item) {
      if (item.limitMin > item.maximumValue - 10) {
        return
      }
      updateTemperatureMinimum(this.$store, {target: {id: item.id, value: item.limitMin + 10}})
    },
    minimumDecrement: function (item) {
      if (item.limitMin < 10) {
        return
      }
      updateTemperatureMinimum(this.$store, {target: {id: item.id, value: item.limitMin - 10}})
    },
    maximumIncrement: function (item) {
      if (item.limitMax > item.maximumValue - 10) {
        return
      }
      updateTemperatureMaximum(this.$store, {target: {id: item.id, value: item.limitMax + 10}})
    },
    maximumDecrement: function (item) {
      if (item.limitMax < 10) {
        return
      }
      updateTemperatureMaximum(this.$store, {target: {id: item.id, value: item.limitMax - 10}})
    }
  }
}
</script>

<style scoped>
</style>
