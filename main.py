from aiohttp import web
from datetime import datetime


routes = web.RouteTableDef()

def show_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


@routes.get('/')
async def hello(request):
    # text = """<meta http-equiv="refresh" content="1" />""" + show_time()
    return web.Response(text =  """<meta http-equiv="refresh" content="1" /> 
    Hello World!<br>The current time is {}.""".format(datetime.strftime(datetime.now(), "%d %B %Y %X")))

    # return web.Response(text=text)

app = web.Application()
app.add_routes(routes)
web.run_app(app)


async def update_timer():
    pass