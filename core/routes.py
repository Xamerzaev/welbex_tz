from flask import render_template, request, redirect, url_for, flash
from core import app
from core.models import db, Wel


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    wels = Wel.query.order_by.paginate(page=page, per_page=2)
    return render_template('index.html', wels=wels)