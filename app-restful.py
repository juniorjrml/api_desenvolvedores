#  Foi deixado a versão antiga
#  no app.py para comparação
import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# BD
DESENVOLVEDORES = [
    {"nome": "junior", "habilidades": ["python", "flask"]},
    {"nome": "jan", "habilidades": ["python", "django", ""]}]
#  Mensagens de erros e estado
SUCESSO = "sucesso"
FALHA = "erro"
mensagem = "Erro desconhecido"
estado = {"status": FALHA, "mensagem": mensagem}

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = DESENVOLVEDORES[id]

        except IndexError:
            estado["mensagem"] = "Registro não localizado"
            response = estado

        except Exception:
            response = estado

        return response


    def put(self, id):
        try:
            dados = json.loads(request.data)
            DESENVOLVEDORES[id] = dados
            response = DESENVOLVEDORES[id]

        except IndexError:
            estado["mensagem"] = "Registro não localizado"
            response = estado

        except Exception:
            response = estado

        return response


    def delete(self, id):
        try:
            DESENVOLVEDORES.pop(id)
            estado["status"] = SUCESSO
            estado["mensagem"] = "registro excluido com sucesso"
            response = estado

        except IndexError:
            estado["mensagem"] = "Registro não localizado"
            response = estado

        except Exception:
            response = estado

        return response


class ListaDeDesenvolvedores(Resource):
    def get(self):
        lista_retorno = {}
        for d in enumerate(DESENVOLVEDORES):
            lista_retorno[d[0]] = d[1]
        return lista_retorno


    def post(self):
        dados = json.loads(request.data)
        print(type(dados))
        DESENVOLVEDORES.append(dados)
        estado["status"] = SUCESSO
        estado["mensagem"] = "Registro incluido com sucesso"
        return estado


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDeDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)