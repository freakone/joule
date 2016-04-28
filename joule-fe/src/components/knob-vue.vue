<template lang="jade">
  div(id="knob-{{ id }}")
</template>

<script>
import Knob from 'knob'

export default {
  props: ['id'],
  ready () {
    var options = {
      label: 'knob-' + this.id,
      value: 60,
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
      options.width = document.getElementById('knob-' + id).offsetWidth
      var newKnob = Knob(options)
      el.replaceChild(newKnob, el.childNodes[0])
    }
    )
  }
}
</script>

<style scoped>
</style>
