import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'recipes.json'))

if not os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    except Exception as e:
        print(f"Error creating the file {DATA_FILE}: {e}")

def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {DATA_FILE}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {DATA_FILE}")
        return []

def write_data(data):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error writing to the file {DATA_FILE}: {e}")

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipes = read_data()
    recipe_id = len(recipes) + 1
    new_recipe = {
        "id": recipe_id,
        "name": data['name'],
        "description": data.get('description', ''),
        "category": data.get('category', ''),
        "ratings": []
    }
    recipes.append(new_recipe)
    write_data(recipes)
    return jsonify(new_recipe), 201

@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(read_data())

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipes = read_data()
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify(recipe)

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.get_json()
    recipes = read_data()
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    recipe.update({
        "name": data['name'],
        "description": data.get('description', recipe['description']),
        "category": data.get('category', recipe['category'])
    })
    write_data(recipes)
    return jsonify(recipe)

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipes = read_data()
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    recipes.remove(recipe)
    write_data(recipes)
    return jsonify({'message': 'Recipe deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
