from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def handler(requests: web.Request):
    return {}


@aiohttp_jinja2.template('result.html')
async def predict_handler(requests: web.Request):
    data = await requests.post()
    print(data)
    return {}




