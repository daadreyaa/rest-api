from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name':'C'}, {'name':'C++'}, {'name': 'Python'}]

@app.route('/', methods=['GET'])
def home():
	return jsonify({'This':'Works'})

@app.route('/lang', methods=['GET'])
def returnall():
	return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name']	 == name]
	return jsonify({'output':langs}) 

@app.route('/lang', methods=['POST'])
def AddOne():
	lang = {'name' : request.json['name']}
	languages.append(lang)
	return jsonify({'languages':languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name']	 == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'output':languages})

@app.route('/lang/<string:name>', methods=['DELETE'])
def dleteOne(name):
	langs = [language for language in languages if language['name']	 == name]
	languages.remove(langs[0])
	return jsonify({'output':languages}) 


if __name__ == '__main__':
	app.run(debug = True)

