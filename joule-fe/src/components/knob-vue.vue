<template lang="jade">
  div(id="knob-{{ id }}")
</template>

<script>
import Knob from 'knob'
var knob = ''

export default {
  props: ['id'],
  ready () {
    knob = Knob({
      label: 'knob-' + this.id,
      value: 60,
      angleOffset: -125,
      angleArc: 360,
      min: 0,
      max: 100,
      width: 145,
      readOnly: true
    })
    document.getElementById('knob-' + this.id).appendChild(knob)
  }
}
</script>

<style scoped>
</style>
