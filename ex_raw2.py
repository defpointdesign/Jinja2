from jinja2 import Template

data = ''' {% raw %} Modul Jinja substitutes the 
corresponding value 
instead of defining {{ name }} {% endraw %}'''

# generate a template based on class Template
tm = Template(data)
msg = tm.render(name='Vadim')
print(msg)
