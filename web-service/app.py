import redis
from flask import Flask, request, jsonify

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True) # should be 'redis' if using Docker and 'localhost' if running locally, in our case we are using Docker 

def read_data():
    recipes = redis_client.hgetall("recipes")
    return [eval(recipe) for recipe in recipes.values()] # break line before return

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe_id = redis_client.incr("recipe_id") 
    new_recipe = {
        "id": recipe_id,
        "name": data['name'],
        "description": data.get('description', ''),
        "category": data.get('category', ''),
        "ratings": []
    } # break line after parameters initialization
    redis_client.hset("recipes", recipe_id, str(new_recipe))  
    return jsonify(new_recipe), 201 # break line before return

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = read_data()
    return jsonify(recipes) # break line before return

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = redis_client.hget("recipes", recipe_id)
    if recipe is None: # break line before if statement
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify(eval(recipe)) # break line before return

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.get_json()
    recipe = redis_client.hget("recipes", recipe_id) # break line after parameters initialization
    if recipe is None: # break line before if statement
        return jsonify({'error': 'Recipe not found'}), 404
    recipe = eval(recipe) # break line after if statement
    recipe.update({
        "name": data['name'],
        "description": data.get('description', recipe['description']),
        "category": data.get('category', recipe['category'])
    })
    redis_client.hset("recipes", recipe_id, str(recipe))
    return jsonify(recipe) # break line before return

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    deleted = redis_client.hdel("recipes", recipe_id)
    if not deleted: # break line before if statement
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify({'message': 'Recipe deleted successfully'}) # break line before return also after if statement

@app.route('/set/<key>/<value>')
def set_value(key, value):
    redis_client.set(key, value)
    return f"Key '{key}' set to '{value}'" # break line before return also after if statement

@app.route('/get/<key>')
def get_value(key):
    value = redis_client.get(key)
    if value is None: # break line before if statement
        return f"Key '{key}' not found", 404
    return f"Key '{key}' has value '{value}'" # break line before return also after if statement


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
