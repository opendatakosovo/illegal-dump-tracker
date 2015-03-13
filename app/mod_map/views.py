from flask import Blueprint, render_template
from flask.views import View

from app import mongo

mod_map = Blueprint('map', __name__)

@mod_map.route('/', methods=['GET'])
def map():
    '''
    Show map
    '''
    return render_template('mod_map/map.html')


