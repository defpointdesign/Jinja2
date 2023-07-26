from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Volkswagen', 'price': 21300},
]
# tpl = "Total car price {{ cs | sum(attribute='price') }}"
# tpl = "Max car price {{ cs | max(attribute='price') }}"
# tpl = "Max car model price {{ (cs | max(attribute='price')).model }}"
tpl = "Random select car {{ cs | random }}"
# tpl = "Uppercase letters {{ cs | replace("s", "S") }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)



digs = [1, 2, 3, 4, 5]
tpl_digs = "Total digit price {{ gs | sum }}"

tm_digs = Template(tpl_digs)
msg_digs = tm_digs.render(gs=digs)
print(msg_digs)