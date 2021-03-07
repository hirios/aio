##from aiohttp import web
##
##routes = web.RouteTableDef()
##
##@routes.get('/')
##async def hello(request):
##    return web.Response(text="Hello, world")
##
##app = web.Application()
##app.add_routes(routes)
##web.run_app(app)


from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def get_planet_ephmeris(request):
    return web.json_response('alan')


app = web.Application()
app.add_routes(routes)

web.run_app(app, host="localhost", port=8080)
