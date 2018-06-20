<!-- This raw tag followed by the script tag is what is needed, We do not include anything because this does not call any components  -->
{% raw %}
<script>
var navi = {
    template: `
    <div>
        <h1 class="has-text-info"> Welcome </h1>
    </div>
    `,
    name: "navi",
    data() {
        return {};
    }
};
</script>
{% endraw %}