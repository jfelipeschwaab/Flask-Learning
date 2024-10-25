from flask import Flask

app = Flask(__name__) ##Creating a object Flask e o seu nome


@app.route('/') ##Request from differents URL's podem ser direcionadas a endpoints diferentes, esse processo é chamado routing
def home():
    return '<h1>Hello, world!</h1>'


"""
1. Routing
Para construir uma rota, primeiro deve-se definir uma função, conhecida como view function, que contém o código necessário para processar
a request e gerar sua resposta. A resposta pode ser algo simples como uma string de texto. Depois, utilizamos o route(), que é um decorador
que atribui uma url para a view function, para ela ser chamada assim que essa url for acessada.
"""


#O route decorator recebe o path da URL como parâmetro, ou a parte da url que contém o nome do domínio, todas as urls devem começar com uma barra '/'
#Multiplas URL's podem ser atribuídas à mesma view
#ex:
"""
@app.route('/')
@app.route('/home')
def home():
    return 'Hello, World!'
"""
@app.route('/reporter')
def reporter():
    return 'Reporter Bio'


"""
2. Render HTML
A resposta que retornamos de uma view function não está limitada apenas à texto ou data. Pode-se retornar também um HTML 

ex: 
@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'
    
    
pode-se usar também triple quotes para multi-line code:

@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>Hello, World!</h1>
    <p>My first paragraph.</p>
    <a href="https://www.codecademy.com">CODECADEMY</a>
    '''
"""


@app.route('/reporter')
def reporter():
    return '''
                <h2>Reporter Bio</h2>
                <a href="/">Return to home page</a>
            '''
            

"""
3. Variable Rules

Vamos ver agora como usar variáveis para utilizar url's dinâmicas

Quando especificamos a url à view function, temos a opção de colocar variáveis entre os parênteses

ex: 
@app.route('/orders/<user_name>/<int:order_id>')


note que podemos opcionalmente forçar o tipo da variável, utilizando a sintaxe: <converter:variable_name>

tipos:

<string:variable> #PADRÃO
<int:variable>
<float:variable>
<path:variable> esse é igual a string, mas aceita /
<uuid:variable> aceita UUID Strings
"""


@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''
    
    
@app.route('/article/<article_name>')
def article(article_name):
    
    return (f'''
            <h2>{article_name.replace('-',' ').title()}</h2>
            <a href="/">Return back to home page</a>
            ''')