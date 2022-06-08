from aiohttp import web
import aiohttp_jinja2

from app.core.prompt import predict


@aiohttp_jinja2.template('index.html')
async def handler(requests: web.Request):
    return {}


@aiohttp_jinja2.template('finish.html')
async def finish_handler(requests: web.Request):
    data = await requests.post()
    file = open('C:\\Users\\rusnak\\PycharmProjects\\mechanical_poetry\\src\\app\\stats.txt', 'a')
    file.write(str(data))
    file.close()
    return {}


@aiohttp_jinja2.template('result.html')
async def predict_handler(requests: web.Request):
    text = await predict(requests)
    num_rows = str(len(text.split('\n')) + 5)
    return {'text': text, 'num_rows': num_rows}
