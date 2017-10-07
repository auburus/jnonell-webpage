from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader = FileSystemLoader('./templates'),
    autoescape = select_autoescape(['html'])
)

template = env.get_template('index.html')
a = template.render(var="World")
print(a)
