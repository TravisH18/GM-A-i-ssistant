from sanic import Blueprint
from .encounterBlueprint import encounter
from .homebrewBlueprint import homebrew

# Define /api (/api/__init__.py)
api = Blueprint.group(encounter, homebrew, url_prefix="/api")