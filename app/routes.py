from flask import Blueprint, render_template, request, redirect, url_for


#The API in this code is represented by the routes defined in the app/routes.py file. An API (Application Programming Interface) in a Flask web application provides endpoints (or URLs)
#that the client—whether a web browser or another service—can call to interact with the application.

main = Blueprint('main', __name__) #This groups related routes together under a "main" blueprint, acting as the starting point for defining endpoints.

items = []  # This will store items in memory

@main.route('/')
def index():
    return render_template('index.html', items=items) #This endpoint handles GET requests to the root URL (http://127.0.0.1:5000/) and serves the index.html template, 
                                                       #passing the list of grocery items (items) for display.

@main.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        items.append(item_name)
        return redirect(url_for('main.index'))
    return render_template('add_item.html')
    
#Explanation: This endpoint supports both GET and POST requests:
             '''GET: Renders the add_item.html form where users can input a new item.
                POST: Processes the form submission, adds the new item to the items list, and redirects to the home route to display the updated list.

These routes provide a simple API for interacting with the grocery app:

    The index route serves the grocery list (like a read operation in CRUD).
    The add_item route allows users to add new items (like a create operation in CRUD).'''


@main.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    # Remove item from list using the index (item_id)
    if 0 <= item_id < len(items):
        del items[item_id]
    return redirect(url_for('main.index'))

#Explanation:
'''This would expose an API endpoint at /api/items to return the grocery list in JSON format, making it suitable for 
integration with other applications or front-end frameworks.'''
