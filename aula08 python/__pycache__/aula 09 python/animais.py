from flask import Flask 
from http import HTTPStatus

pessoas = [
	{
		'id': 1,
		'nome': 'Café',
		'especie': 'Gato'
	},
	{
		'id': 2,
		'nome': 'Margot',
		'idade': '25'
	},
	{
		'id': 3
		'nome': 'Andre'
		'idade': 38
		
    },
]
app = Flask(__name__) 
app.json.sort_keys = False # Teste e depois tire a linha para ver o que acontece.

@app.route('/pessoas')
def listar_pessoas():
	return pessoas
	
if __name__ == '__main__':
    app.run(debug=True)