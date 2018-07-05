<!-- This raw tag followed by the script tag is always needed -->
{% raw %}
<template id="home">
  <div>
    <h1>{{ action }}</h1>
    <p> {{ status }} </p>
    <contained></contained>
    <work working="creating more components"></work>
  </div>
</template>
<script src="work.vue" type="module"></script>
<script src="contained.vue" type="module"></script>
<script>
var home = {
    props: ["action"],
    template: "#home",
    components: { work, contained },
    data() {
        return {
            status: "The component loaded successfully."
        };
    }
};
</script>
{% endraw %}