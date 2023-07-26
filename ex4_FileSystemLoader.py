from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Alex", "old": 32, "weigth": 80.2},
    {"name": "Nikolas", "old": 28, "weigth": 75.5},
    {"name": "Ivan", "old": 40, "weigth": 94.0},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html') #Template
msg = tm.render(users=persons)

print(msg)