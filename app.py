# Going through Sanic application basic tutorial

from sanic import Sanic, Database

app = Sanic("MyApp")
@app.before_server_start
async def attach_db(app, loop):
    app.ctx.db = Database() # attach database to the Apps ctx (context) object.