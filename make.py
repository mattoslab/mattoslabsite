from jinja2 import Template
import shutil
import yaml
import markdown

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('.'),
                  extensions=['jinja2.ext.with_'])

env.filters.update({
    'markdown': lambda text: markdown.markdown(text)
})

with open('content/pages.yml') as f:
    PAGES = yaml.load(f)

with open('content/people.yml') as f:
    LAB_MEMBERS = yaml.load(f)

with open('content/projects.yml') as f:
    PROJECTS = yaml.load(f)

with open('content/publications.yml') as f:
    PUBLICATIONS = yaml.load(f)

PAGE_CONTEXT = {
    'people.html': {
        'lab_members': LAB_MEMBERS,
    },
    'research.html': {
        'projects': PROJECTS,
    },
    'publications.html': {
        'publications': PUBLICATIONS,
    }
}


def make_html(page):
    template = env.get_template('pages/{template}'.format(**page))

    html = template.render(
        active_page=page,
        pages=PAGES,
        **PAGE_CONTEXT.get(page['href'], {})
    )

    with open('build/{}'.format(page['href']), 'w') as f:
        f.write(html.encode('utf-8'))


def copy_static():
    try:
        shutil.rmtree('build/static')
    except OSError:
        pass

    shutil.copytree('static', 'build/static')


def make():
    copy_static()
    for page in PAGES:
        make_html(page)


if __name__ == '__main__':
    make()
