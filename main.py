from flask import Flask, render_template

app = Flask(__name__)

locks = [
    {"id": 1, "name": "Замок 1", "price": 100},
    {"id": 2, "name": "Замок 2", "price": 150},
    {"id": 3, "name": "Замок 3", "price": 200},
]

@app.route('/')
def index():
    locks_with_str_id = [{"id": lock["id"], "name": lock["name"], "price": lock["price"], "lock_id_str": str(lock["id"])} for lock in locks]
    return render_template('index.html', locks=locks_with_str_id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/assortment')
def assortment():
    return render_template('assortment.html')

@app.route('/buy/<int:lock_id>')
def buy(lock_id):
    selected_lock = next((lock for lock in locks if lock["id"] == lock_id), None)
    if selected_lock:
        return f'Вы успешно купили замок: {selected_lock["name"]} за {selected_lock["price"]} руб.'
    else:
        return 'Такого замка не существует.'

if __name__ == '__main__':
    app.run(debug=True)
