from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

items = []  # This will store items in memory

@main.route('/')
def index():
    return render_template('index.html', items=items)

@main.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        items.append(item_name)
        return redirect(url_for('main.index'))
    return render_template('add_item.html')

@main.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    # Remove item from list using the index (item_id)
    if 0 <= item_id < len(items):
        del items[item_id]
    return redirect(url_for('main.index'))
