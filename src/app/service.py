from app.routes import setup_route
from app.utils.configurator import get_config
from app.utils.logs import init_logger
from app.core.prompt import load_poetry_generator

import sys
import jinja2
import aiohttp_jinja2
from aiohttp import web


def init_app(argv):
    app = web.Application()
    app['config'] = get_config(argv)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates/'))
    app['static_root_url'] = 'static/'
    app['poetry_generator'] = load_poetry_generator()
    init_logger(app['config'])
    setup_route(app)
    return app


def start(argv):
    app = init_app(argv)
    service_config = app['config']['service']
    web.run_app(
        app,
        port=service_config['port'],
        host=service_config['host'],
    )


if __name__ == '__main__':
    start(sys.argv[1:])
