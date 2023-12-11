# Import libraries for Flask framework, HTML template, and handling HTTP requests 
from flask import Flask 
from flask import render_template, request
import requests

# Create Flask application instance 
app = Flask(__name__)

# Define API URL and headers 
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "d2f7c75442mshde016465b174ed9p10a7b5jsn1acedf7fc107",
  }

# Define API endpoints to retrieve different stuff 
random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"

# Route handler 
@app.route('/')
def search_page():

# Fetch random food-related joke & render on search page  
# Change: removed str() conversion and work with response object directly 
  joke_response = requests.request("GET", url + random_joke, headers=headers)
  joke_data = joke_response.json()
  joke_text = joke_data.get('text', 'No joke available')  # Handle the case where 'text' is not in the response
  print(joke_text)
  return render_template('search.html', joke=joke_text)

@app.route('/recipes')
def get_recipes():
  # Check for ingredients 
  if (str(request.args['ingredients']).strip() != ""):
      # If there is a list of ingridients -> list
      querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingredients']}
      # Send HTTP GET request to API using 'find' endpoint, converted to JSON format
      response = requests.request("GET", url + find, headers=headers, params=querystring).json()
      # Render on recipes.html template
      return render_template('recipes.html', recipes=response)
  else:
      # Random recipes
      querystring = {"number":"5"}
      response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
      print(response)
      return render_template('recipes.html', recipes=response['recipes'])

# Run Flask application 
if __name__ == '__main__':
  # Flask debug mode 
  app.debug = True
  app.run()

  


  