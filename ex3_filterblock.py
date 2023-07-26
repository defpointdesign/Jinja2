from jinja2 import Template

persons = [
    {"name": "Alex", "old": 32, "weigth": 80.2},
    {"name": "Nikolas", "old": 28, "weigth": 75.5},
    {"name": "Ivan", "old": 40, "weigth": 94.0},
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''
tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)
