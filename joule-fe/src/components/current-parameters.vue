<template lang="jade">
  .row
    .col-md-10
      .col-md-6
        .box.box-primary
          .box-header.with-border
            h3.box-title Temperatura 1
          .box-body
            vue-chart(:chart-type="LineChart", :columns="columns", :rows="rows", :options="options")

        .box.box-primary
          .box-header.with-border
            h3.box-title Temperatura 2
          .box-body
            vue-chart(:chart-type="LineChart", :columns="columns", :rows="rows", :options="options")

      .col-md-6
        .box.box-primary
          .box-header.with-border
            h3.box-title Temperatura 3
          .box-body
            vue-chart(:chart-type="LineChart", :columns="columns", :rows="rows", :options="options")

        .box.box-primary
          .box-header.with-border
            h3.box-title Temperatura 4
          .box-body
            vue-chart(:chart-type="LineChart", :columns="columns", :rows="rows", :options="options")
    .col-md-2
      .row
        .info-box
          span.info-box-icon.bg-red
          .info-box-content
            span.info-box-text Pompa 1
      .row
        .info-box
          span.info-box-icon.bg-green
          .info-box-content
            span.info-box-text Pompa 2


  .row
    .col-md-10
      .col-md-2
        .box.box-primary
          .box-header.with-border
            h3.box-title Fan 1
          .box-body
            knob#first
      .col-md-2
        .box.box-primary
          .box-header.with-border
            h3.box-title Fan 2
          .box-body
            knob#second
      .col-md-2
        .box.box-primary
          .box-header.with-border
            h3.box-title Fan 3
          .box-body
            knob#third
      .col-md-2
        .box.box-primary
          .box-header.with-border
            h3.box-title Fan 4
          .box-body
            knob#fourth
      .col-md-2
        .box.box-primary
          .box-header.with-border
            h3.box-title Fan 5
          .box-body
            knob#fifth
</template>

<script>
import Knob from './knob-vue'
export default {
  components: {
    Knob
  },
  data () {
    return {
      columns: [{
        'type': 'number',
        'label': 'Timestamp'
      },
      {
        'type': 'number',
        'label': '*C'
      }],
      rows: [
        [123456, 0],
        [123457, 100],
        [123458, 200]
      ],
      options: {
        hAxis: {
          title: 'Timestamp'
        },
        vAxis: {
          title: 'Temperature',
          minValue: 0,
          maxValue: 1000
        },
        height: 200,
        curveType: 'function'
      }
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
