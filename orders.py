from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.order import Order
from flask_app.models.user import User


@app.route('/new/order')
def new_order():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new.html',user=User.get_by_id(data))