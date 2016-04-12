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
      | BOK
</template>

<script>
export default {
  data () {
    return {
      columns: [{
        'type': 'string',
        'label': 'Year'
      }, {
        'type': 'number',
        'label': 'Sales'
      }, {
        'type': 'number',
        'label': 'Expenses'
      }],
      rows: [
        ['2004', 1000, 400],
        ['2005', 1170, 460],
        ['2006', 660, 1120],
        ['2007', 1030, 540]
      ],
      options: {
        hAxis: {
          title: 'Year',
          minValue: '2004',
          maxValue: '2007'
        },
        vAxis: {
          title: '',
          minValue: 300,
          maxValue: 1200
        },
        height: 300,
        curveType: 'function'
      }
    }
  }
}
</script>

<style scoped>
</style>
