from flask import Blueprint, render_template
from flask.views import View
from flask import Response
from bson import json_util

from app import mongo

import requests
import json

mod_api = Blueprint('api', __name__, url_prefix = '/api')

@mod_api.route('/routes/<route_slug>', methods=['GET'])
def route(route_slug):

	'''
	Hardcoded for now, but this should be a MongoDB query
	that fetches the document where { 'slug': route_slug }
	'''
	route_merc_kalt = {
		'name': 'Merc.Kalt.03 802 AM',
		'slug': 'merc-kalt-03-802-am',
		'coordinates':[
			{
				'lng': 20.4265936,
				'lat': 42.388864,
				'weight': 100
			},
			{
				'lng': 20.4266192,
				'lat': 42.3888352,
				'weight': 1
			},
			{
				'lng': 20.4267232,
				'lat': 42.3888256,
				'weight': 1
			},
			{
				'lng': 20.426744,
				'lat': 42.3888288,
				'weight': 1
			},
			{
				'lng': 20.4267904,
				'lat': 42.3888576,
				'weight': 2
			},
		]
	}

	route_merc_cist = {
		'name': 'Merc.Cist.03631BC',
		'slug': 'merc-cist-03631bc',
		'coordinates':[
			{
				'lng': 20.4265136,
				'lat': 42.3889248,
				'weight': 53
			},
			{
				'lng': 20.426496,
				'lat': 42.3887168,
				'weight': 1
			},
			{
				'lng': 20.4265392,
				'lat': 42.3887776,
				'weight': 1
			},
			{
				'lng': 20.4265904,
				'lat': 42.3888576,
				'weight': 68
			}
		]
	}

	route_coordinates = []
	if route_slug == 'merc-kalt-03-802-am':
		route_coordinates = route_merc_kalt['coordinates']
	elif route_slug == 'merc-cist-03631bc':
		route_coordinates = route_merc_cist['coordinates']
    
	resp = Response(
            response=json_util.dumps(route_coordinates),
            mimetype='application/json')

	return resp