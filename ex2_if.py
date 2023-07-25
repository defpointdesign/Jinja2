from jinja2 import Template

cities = [{'id': 1, 'city': 'Netishyn'},
          {'id': 5, 'city': 'Ostrih'},
          {'id': 7, 'city': 'Slavuta'},
          {'id': 8, 'city': 'Iziaslav'},
          {'id': 11, 'city': 'Shepetivka'},]
link = ''' <select name="cities">
{%for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == 'Netishyn' -%}
    <option>{{c['city']}}</option>
    
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
