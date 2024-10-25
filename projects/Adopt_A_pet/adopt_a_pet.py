from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
    return ('''
            <h1>Adopt a Pet!</h1>
            <p>Browse through the links below to find your new furry friend:</p>
            <ul>
            <li>Dogs</li>
            <li>Cats</li>
            <li>Rabbits</li>
            </ul>
            ''')
    
@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type}</h1>'
    html += '<ul>'
    for pet_id, animal in enumerate(pets[pet_type]):
        html += f'<a href="/animals/{pet_type}/{pet_id}"><li>{animal["name"]}</li></a>'
    html += '</ul>'
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    
    return (f'''
            <h1>{pet["name"]}</h1>
            <img href={pet["url"]}></img>
            <p>{pet["description"]}</p>
            <ul>
                <li>{pet["breed"]}</li>
                <li>{pet["age"]}</li>
            </ul>
            ''')
    