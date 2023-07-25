from jinja2 import Template
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

per = Person("Vadim", 25)
tm = Template("I am {{p.getAge() }}, and my name {{ p.getName() }}.")
msq = tm.render(p=per)
print(msq)