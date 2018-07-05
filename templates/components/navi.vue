<!-- This raw tag followed by the script tag is what is needed, We do not include anything because this does not call any components  -->
{% raw %}
<template id="navi">
    <div>
        <h1 class="has-text-info"> Welcome </h1>
    </div>
</template>
<script>
var navi = {
    template: "#navi",
    data() {
        return {};
    }
};
</script>
{% endraw %}
