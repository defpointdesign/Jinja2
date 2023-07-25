from jinja2 import Template
link = ''' In HTML documents links are defined like this:
<a href="#">Link</a>'''

tm = Template("{{ link | e}}")
msg = tm.render(link=link)
print(msg)
