from flask import Flask, render_template

app = Flask(__name__)

class cadpokemon:
    def __init__(self, numero, nome, tipo, altura, peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'



@app.route('/pokemon')
def pokemon():
    pk1 = cadpokemon(4, "Chamander", "Fogo", 0.7,5)
    pk2 = cadpokemon(1, "Bulbasaur", "Grama", 0.5,6)
    pk3 = cadpokemon(25, "Pikachu", "Elétrico", 0.6, 4)
    lista = [pk1,pk2,pk3]
    return render_template('Pokemon.html', Titulo ="Pokémons Iniciais: ", ListaPokemons = lista)


if __name__ == '__main__':
    app.run()
