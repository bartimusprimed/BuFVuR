<!-- Because this component uses the test component, we must include it before anything  -->
{% include 'components/work.vue' %}
<!-- This raw tag followed by the script tag is always needed -->
{% raw %}
<script>
var home = {
    props: ["action"],
    name: "home",
    template: `
    <div>
        <h1>{{ action }}</h1>
        <p> {{ status }} </p>
        <test work="creating more components"></test>
    </div>
    `,
    components: { test },
    data() {
        return {
            status: "The component loaded successfully."
        };
    }
};
</script>
{% endraw %}