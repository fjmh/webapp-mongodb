# -*- coding: utf-8 -*-
from bottle import get, post, template, request, response, run
from pymongo import MongoClient
from bson.json_util import dumps

@get('/index')
def index():
        return template('index.tpl')

@post('/connection')
def connection():
	username = request.forms.get("username")
	password = request.forms.get("password")
	ip = request.forms.get("ip")
	port = request.forms.get("port")
	database = request.forms.get("database")

	mongoDB_server_uri = "mongodb://%s:%s@%s:%s/%s" % (username, password, ip, port, database)

	client = MongoClient(mongoDB_server_uri)

	db = client[database]
	collection = db['comunidades']
	data = collection.find()
	data_dumps = dumps(data)

	output = template('connection', data_in_connection_tpl = data_dumps) 

	return output


run(host='localhost', port=8080)
