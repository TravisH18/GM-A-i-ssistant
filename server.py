from sanic import Sanic, Database
from sanic_ext import render
from sanic.response import text
from .config import MyConfig
from .api import api

# For jinja template info 
# https://sanic.dev/en/plugins/sanic-ext/templating/jinja.html#quotstaticquot-redirects
# @app.get("/")
# @app.ext.template("foo.html")
# async def render_index(request: Request):
#     return text("Hello, world.")
def create_app(config=MyConfig) -> Sanic:
        app = Sanic(__name__, config=config)
        app.blueprint(api)
        return app


if __name__ == "__main__":

    app = create_app
    @app.before_server_start
    async def attach_db(app, loop):
            app.ctx.db = Database()

    app.run()

    @app.after_server_stop
    async def close_app(app):
           return "! Server ended !"