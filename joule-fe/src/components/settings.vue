<template lang="jade">
  section.content-header
    h1
      | Ustawienia
  section.content
    .row
      .col-md-6
        .box.box-primary
          .box-header.with-border
            h3.box-title Ogólne
          .box-body
            input.form-control(type="text", placeholder="Nazwa kotła", :value="generalSettings.name", @change="updateName")
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

    .row
      .col-md-3(v-for="item in temperatureSensors")
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
                .col-xs-2
                  | Minimum
                .col-xs-6
                  mdl-slider(:value="item.limitMin", :id="item.id", @change="updateTemperatureMinimum" min="0" max="1000")
                .col-xs-4
                  input.form-control(type="text", :value="item.limitMin", disabled)
            .row
                .col-xs-2
                  | Maximum
                .col-xs-6
                  mdl-slider(:value="item.limitMax", :id="item.id", @change="updateTemperatureMaximum" min="0" max="1000")
                .col-xs-4
                  input.form-control(type="text", :value="item.limitMax", disabled)
</template>

<script>
import { digitalOutputs, analogOutputs, temperatureSensors, generalSettings } from '../vuex/getters'
import { updateName, updateAnalogOutputName, updateDigitalOutputName, updateTemperatureMaximum, updateTemperatureMinimum, updateTemperatureSensorName } from '../vuex/actions'

export default {
  vuex: {
    getters: {
      analogOutputs: analogOutputs,
      digitalOutputs: digitalOutputs,
      temperatureSensors: temperatureSensors,
      generalSettings: generalSettings
    },
    actions: {
      updateName,
      updateAnalogOutputName,
      updateDigitalOutputName,
      updateTemperatureMaximum,
      updateTemperatureSensorName,
      updateTemperatureMinimum
    }
  }
}
</script>

<style scoped>
</style>
