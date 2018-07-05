<!-- Use template and script tags, nested inside the {% raw %} {% endraw %}  -->
{% raw %}
<template id="contained">
  <div v-bind:style="style">
    {{ test }}
  </div>
  
</template>

<script>
var contained = {
  data () {
    return {
      test: "This is a single file test component",
      style: `
        font-size: 1.3rem;
        background-color: black;
        `
    }
  },
  template: "#contained"
}
</script>
{% endraw %}