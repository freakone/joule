<template lang="jade">
  section.content-header
    h1
      | Sterowanie
  section.content
    .row
      .col-md-3
        .box.box-primary
          .box-header.with-border
            h3.box-title Pompa 1
            .box-tools
              mdl-switch(:checked.sync="checked")
        .box.box-primary
          .box-header.with-border
            h3.box-title Pompa 2
            .box-tools
              mdl-switch(:checked.sync="checked")
      .col-md-3
        .box.box-primary
          .box-header.with-border
            h3.box-title Wentylator 1
            .box-slider
              mdl-slider(:value.sync="amount" min="0" max="100")
        .box.box-primary
          .box-header.with-border
            h3.box-title Wentylator 2
            .box-slider
              mdl-slider(:value.sync="amount" min="0" max="100")

       .col-md-3
        .box.box-primary
          .box-header.with-border
            h3.box-title Pompa 3
            .box-tools
              mdl-switch(:checked.sync="checked")
        .box.box-primary
          .box-header.with-border
            h3.box-title Pompa 4
            .box-tools
              mdl-switch(:checked.sync="checked")
      .col-md-3
        .box.box-primary
          .box-header.with-border
            h3.box-title Wentylator 3
            .box-slider
              mdl-slider(:value.sync="amount" min="0" max="100")
        .box.box-primary
          .box-header.with-border
            h3.box-title Wentylator 4
            .box-slider
              mdl-slider(:value.sync="amount" min="0" max="100")




</template>

<script>
</script>

<style scoped>
  .box-slider {
    position: absolute;
    top: 10px;
    right: 5px;
    width: 60%;
  }
</style>
