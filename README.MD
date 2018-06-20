# What is BuFVur?
I am a python guy, but I recently got into frontend development. I had a lot of experience with Django, and was loving it. I stumbled on VueJS and really liked it. So while learning there were so many times that I wish I could just do a quick layout with a VueJS frontend and a simple python backend. Django was too much so I started using Flask.

So I decided to create a rapid prototype environment using flask as the backend, rethinkdb as the database, and vuejs with bulma as the frontend.

## How is this easier?
I am just really comfortable with python as a backend. If I am learning something new, then I like to just concentrate on that.

### Explain...

- You create a "COMPONENTNAME.vue" file in the templates/components directory.
- You can include that file with jinja2 include 
`{% include 'components/COMPONENTNAME.vue' %}`
- Add it to the components
- Use the component in the template.
- Bulma is included component wide.