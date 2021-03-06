from flask import render_template, request, redirect, url_for, flash
from core import app
from core.models import db, Wel


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    wels = Wel.query.paginate(page=page, per_page=5)
    return render_template('index.html', wels=wels)