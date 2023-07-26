from jinja2 import Template

persons = [
    {"name": "Alex", "old": 32, "weigth": 80.2},
    {"name": "Nikolas", "old": 28, "weigth": 75.5},
    {"name": "Ivan", "old": 40, "weigth": 94.0},
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%-endfor %}
</ul>
{% endmacro %}

{% call (user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weigth: {{user.weigth}}
    </ul>
{% endcall %}
'''
tm = Template(html)
msg = tm.render(users=persons)

print(msg)