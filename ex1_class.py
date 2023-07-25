from jinja2 import Template
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person("Vadim", 25)
tm = Template("I am {{ p.age }} old, my name {{ p.name }}.")
msq = tm.render(p=per)
print(msq)