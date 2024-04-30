#!/usr/bin/python3

# This file is intentionally not formatted according to PEP8
# to avoid linter warnings about wildcard imports.

from flask import Blueprint

app_views = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Wildcard import of everything from api.v1.views.index
from . import index  # PEP8 warning is expected here
