from jinja2 import Template
name = "Vadim"
age = 28
# create template
tm = Template("I am {{ a*2 }} old, my name {{n.upper()}}")

msg = tm.render(n=name, a=age)
print(msg)




