from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретний ключ для flash повідомлень

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка реєстрації (Фейкова)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Реєстарція лише для математиків', 'danger')
        return redirect(url_for('register'))
    
    return render_template('register.html')

# Сторінка успішного входу
@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        word = request.form.get('wordInput', '').strip().lower()
        if word == 'chef':
            return redirect(url_for('temporary_end'))  # Перенаправлення на temporary_end.html
    
    return render_template('success.html')


@app.route('/login', methods=['POST'])
def login():
    first_name = request.form.get('first_name', '').strip().lower()
    last_name = request.form.get('last_name', '').strip().lower()
    
    # Перевіряємо ім'я та прізвище (без врахування регістру)
    if first_name == "степан" and last_name == "банах":
        return redirect(url_for('success'))
    
    # Якщо неправильні дані – флеш-повідомлення
    flash('Невідома соба', 'danger')
    return redirect(url_for('index'))

# Сторінка "temporary_end"
# @app.route('/temporary_end')
# def temporary_end():
#     return render_template('temporary_end.html')

# API для генерації випадкового числа
@app.route('/random-number')
def get_random_number():
    numbers = [30] * 15 + [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  # 30 випадає частіше
    return jsonify({'random_number': random.choice(numbers)})

@app.route('/temporary_end', methods=['GET', 'POST'])
def temporary_end():
    if request.method == 'POST':
        word = request.form.get('wordInput', '').strip().lower()
        if word == 'love':  
            return "gay"  # Перенаправлення на нову сторінку
        
    return render_template('temporary_end.html')
    

if __name__ == '__main__':
    app.run(debug=True)







