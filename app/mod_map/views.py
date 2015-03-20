from flask import Blueprint, render_template
from flask.views import View

from app import mongo

mod_map = Blueprint('map', __name__)

@mod_map.route('/', methods=['GET'])
def map():
    '''
    Show map page.
    '''
    return render_template('mod_map/map.html')

@mod_map.route('/statistics', methods=['GET'])
def statistics():
    '''
    Show statistics page.
    '''
    return render_template('mod_map/statistics.html')

@mod_map.route('/about', methods=['GET'])
def about():
    '''
    Show about page.
    '''
    return render_template('mod_map/about.html')

@mod_map.route('/testimonials', methods=['GET'])
def testimonials():
    '''
    Show testimonials page.
    '''
    return render_template('mod_map/testimonials.html')

@mod_map.route('/video', methods=['GET'])
def video():
    '''
    Show video page.
    '''
    return render_template('mod_map/video.html')

