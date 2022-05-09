from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def handler(requests: web.Request):
    return {}


@aiohttp_jinja2.template('finish.html')
async def finish_handler(requests: web.Request):
    data = await requests.post()
    print(data)
    return {}


@aiohttp_jinja2.template('result.html')
async def predict_handler(requests: web.Request):
    data = await requests.post()
    title = data['title']
    poetry_type = data['type']
    text = f"""
    {poetry_type} {title} \n
    I met a traveller from an antique land,
    Who said—“Two vast and trunkless legs of stone
    Stand in the desert. . . . Near them, on the sand,
    Half sunk a shattered visage lies, whose frown,
    And wrinkled lip, and sneer of cold command,
    Tell that its sculptor well those passions read
    Which yet survive, stamped on these lifeless things,
    The hand that mocked them, and the heart that fed;
    And on the pedestal, these words appear:
    My name is Ozymandias, King of Kings;
    Look on my Works, ye Mighty, and despair!
    Nothing beside remains. Round the decay
    Of that colossal Wreck, boundless and bare
    The lone and level sands stretch far away.
    """
    num_rows = str(len(text.split('\n')) + 5)
    return {'text': text, 'num_rows': num_rows}




