import asyncio
from aiohttp import web


async def index(request):
    # return web.Response(text="OK")
    return web.Response(body=b'<h1>index page</h1>',content_type='text/html')

async def main():
    server = web.Server(index)
    await loop.create_server(server, "127.0.0.1", 8080)
    print("======= Serving on http://127.0.0.1:8080/ ======")

    # pause here for very long time by serving HTTP requests and
    # waiting for keyboard interruption
    await asyncio.sleep(100*3600)


loop = asyncio.get_event_loop()

#indextry:
try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
loop.close()
