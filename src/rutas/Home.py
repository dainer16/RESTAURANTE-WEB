from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Home = Blueprint("routes_Home", __name__)


@routes_Home.route('/IndexHome', methods=['GET'] )
def IndexHome():
    
    return render_template('/Main/Home.html')