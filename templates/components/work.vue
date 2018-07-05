<!-- This raw tag followed by the script tag is what is needed, We do not include anything because this does not call any components  -->
{% raw %}
<template id="work">
  <div>
    <h1 class="has-text-info"> Loaded the work component </h1>
    <p class="has-text-weight-bold"> You should be {{ working }} </p>
  </div>
</template>

<script>
// Notice how we create a variable named test. this will make it available to the component that includes it.
var work = {
  name: "work",
  props: ["working"],
  template: "#work",
  data() {
      return {};
  }
};
</script>
{% endraw %}