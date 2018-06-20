<!-- This raw tag followed by the script tag is what is needed, We do not include anything because this does not call any components  -->
{% raw %}
<script>
// Notice how we create a variable named test. this will make it available to the component that includes it.
var test = {
    props: ["work"],
    template: `
    <div>
        <h1> Loaded the work component </h1>
        <p class="has-text-weight-bold"> You should be {{ work }} </p>
    </div>
    `,
    name: "test",
    data() {
        return {};
    }
};
</script>
{% endraw %}