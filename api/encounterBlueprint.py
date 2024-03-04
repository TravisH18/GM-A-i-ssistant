from sanic import Blueprint
from sanic_ext import render

# Define /api/encounter
encounter = Blueprint("encounter", url_prefix="/encounter")

# /api/encounter/
encounter.route("/") # or encounter.get("/")
async def encounter_root(request):
    return await render("encounterBuilder.html", context={"seq": ["one", "two"]})