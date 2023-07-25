from jinja2 import Template

per = {'name': 'Vadim', 'age': 26}
tm = Template("I am {{p['age'] }}, and my name {{ p['name'] }}.")
msq = tm.render(p=per)
print(msq)

