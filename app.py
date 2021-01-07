from flask import Flask, request, jsonify
import json

app = Flask(__name__)
DESENVOLVEDORES = [
    {"id": 0, "nome": "junior", "habilidades": ["python", "flask"]},
    {"id": 1, "nome": "jan", "habilidades": ["python", "django", ""]}]


SUCESSO = "sucesso"
FALHA = "erro"
mensagem = "registro não localizado"
estado = {"status": FALHA, "mensagem": mensagem}


@app.route("/")
def home():
    return "Seja Bem Vindo"




@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    metodo = request.method
    if metodo == 'GET':
        try:
            response = DESENVOLVEDORES[id]
        except IndexError:
            response = estado

    elif metodo == 'PUT':
        try:
            dados = json.loads(request.data)
            DESENVOLVEDORES[id] = dados
            response = DESENVOLVEDORES[id]
        except IndexError:
            response = jsonify(estado)

    elif metodo == 'DELETE':
        try:
            DESENVOLVEDORES.pop(id)
            estado["status"] = SUCESSO
            estado["mensagem"] = "registro excluido com sucesso"
            response = estado
        except:
            response = estado
    return response

@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    metodo = request.method

    if metodo == 'GET':
        lista_retorno = {}
        for d in enumerate(DESENVOLVEDORES):
            lista_retorno[d[0]] = d[1]
        response = lista_retorno

    elif metodo == 'POST':
        dados = json.loads(request.data)
        dados["id"] = len(DESENVOLVEDORES)
        DESENVOLVEDORES.append(dados)
        estado["status"] = SUCESSO
        estado["mensagem"] = "Registro incluido com sucesso"
        response = estado

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

