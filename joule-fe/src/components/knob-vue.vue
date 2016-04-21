<template lang="jade">
  div(id="knob-{{ id }}" disabled)
</template>

<script>
import Knob from 'knob'

export default {
  props: ['id'],
  ready () {
    var knob = Knob({
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
