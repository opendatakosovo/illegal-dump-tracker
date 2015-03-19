from flask import Blueprint, render_template
from flask.views import View
from flask import Response
from bson import json_util
from bson.son import SON
from app import mongo

mod_api = Blueprint('api', __name__, url_prefix = '/api')

@mod_api.route('/routes/<route_slug>', methods=['GET'])
def route(route_slug):

	'''
	Hardcoded for now, but this should be a MongoDB query
	that fetches the document where { 'slug': route_slug }
	'''

	docs = mongo.db.wasteroutes.aggregate([
		{
			"$match":{
				"route.slug": route_slug
			}
		},
		{
			"$group":{
				"_id":{
				 	"rank":"$rank",
				 	"lat": "$lat",
				 	"lng": "$lng"
				},
				"count":{
					"$sum":1
				}
			}
		},
		{
			"$sort": {
				"_id.rank": 1
			}	
		},
		{
			"$project":{
				"_id": 0,
				"lat":"$_id.lat",
				"lng":"$_id.lng",
				"count":"$count"
			}	
		}
	])

	result = docs['result']


	resp = Response(
            response=json_util.dumps(result),
            mimetype='application/json')

	return resp