from jinja2 import Template
import shutil
import yaml
import markdown
import os

from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('.'),
                  extensions=['jinja2.ext.with_'])

env.filters.update({
    'markdown': lambda text: markdown.markdown(text)
})

class FileSystemContentLoader(object):

    def __init__(self, root):
        self.root = root

    def __getitem__(self, item):
        with open(os.path.join(self.root, '{}.yml'.format(item))) as f:
            return yaml.load(f)

CONTENT = FileSystemContentLoader('content')

PAGES = CONTENT['pages']

PAGE_CONTEXT = {
    'people.html': {
        'lab_members': CONTENT['people'],
    },
    'research.html': {
        'projects': CONTENT['projects'],
    },
    'publications.html': {
        'publications': CONTENT['publications'],
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
