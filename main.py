from flask import Flask
from flask import request, jsonify, abort
import json

with open('fakedatabase.json', 'r') as f:
  global data 
  data = json.load(f)

app = Flask(__name__)

@app.route("/contacts", methods=['GET'])
def get_contacts():
    """Return all contacts or filtered if phrase is present in args"""
    if request.method == 'GET':
        args = request.args
        phrase = args.get("phrase")
        people = sorted(data, key=lambda contact: contact['name']) 
        if phrase == "":
            abort(400)
        if phrase:
            phrase = phrase.lower() 
            people = list(filter(lambda contact: phrase in contact.get("name", "").lower(), people))
        return jsonify(people)
    abort(405)

@app.route("/contact/<id>", methods=['GET'])
def get_contact(id):
    """Return contact with the given id, return 404 status code if not found"""
    if request.method == 'GET':
        found_contact = next((contact for contact in data if contact.get("id", "") == id), None)
        if found_contact:
            return jsonify(found_contact)
        abort(404)
    abort(405)

@app.route("/contact/<id>", methods=['DELETE'])
def delete_contact(id):
    """Delete contact with the given id, return 404 status code if not found"""
    if request.method == 'DELETE':
        found_contact = next((contact for contact in data if contact.get("id", "") == id), None)
        if found_contact:
            data.remove(found_contact)
            return '', 204
        abort(404)
    abort(405)