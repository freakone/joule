<template lang="jade">
  div(id="knob-{{ id }}")
</template>

<script>
import Knob from 'knob'

export default {
  props: ['id', 'actual_value'],
  data () {
    return {
      knob: null
    }
  },
  watch: {
    actual_value: 'updateKnobValue'
  },
  methods: {
    updateKnobValue: function () {
      this.knob.setValue(this.actual_value)
    }
  },
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
    this.knob = Knob(options)
    el.appendChild(this.knob)

    window.addEventListener('resize', function (event) {
      var knobDiv = document.getElementById('knob-' + id)
      if (knobDiv) {
        options.width = knobDiv.offsetWidth
        this.knob = Knob(options)
        el.replaceChild(this.knob, el.childNodes[0])
      }
    })
  }
}
</script>

<style scoped>
</style>
