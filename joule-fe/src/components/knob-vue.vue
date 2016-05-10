<template lang="jade">
  div(id="knob-{{ id }}")
</template>

<script>
import Knob from 'knob'

export default {
  props: ['id', 'actual_value'],
  ready () {
    var options = {
      label: 'knob-' + this.id,
      value: this.actual_value,
      angleOffset: -125,
      angleArc: 360,
      min: 0,
      max: 100,
      width: document.getElementById('knob-' + this.id).offsetWidth,
      readOnly: true
    }
    var el = document.getElementById('knob-' + this.id)
    var id = this.id
    el.appendChild(Knob(options))

    window.addEventListener('resize', function (event) {
      var knobDiv = document.getElementById('knob-' + id)
      if (knobDiv) {
        options.width = knobDiv.offsetWidth
        var newKnob = Knob(options)
        el.replaceChild(newKnob, el.childNodes[0])
      }
    }
    )
  }
}
</script>

<style scoped>
</style>
