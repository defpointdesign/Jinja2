from jinja2 import Template
name = "Vadim"

# create template
tm = Template("Hello {{name}}")

msg = tm.render(name=name)
print(msg)



