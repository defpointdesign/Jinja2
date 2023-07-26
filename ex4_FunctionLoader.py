from jinja2 import Environment, FunctionLoader

persons = [
    {"name": "Alex", "old": 32, "weigth": 80.2},
    {"name": "Nikolas", "old": 28, "weigth": 75.5},
    {"name": "Ivan", "old": 40, "weigth": 94.0},
]
def loadTpl(path):
    if path == "index":
        return '''Name {{u.name}}, age {{u.old}}'''
    else:
        return '''Data: {{u}}'''



file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index') #Template
msg = tm.render(u=persons[1])

print(msg)