from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
db_config = {
    'host': 'PRIVATE_IP_OF_MYSQL_INSTANCE',
    'user': 'flask_user',
    'password': 'Admin@123',
    'database': 'todo_app'
}

# Home route
@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        return render_template('index.html', todos=todos)
    finally:
        cursor.close()
        connection.close()

# Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if not task:
        flash("Task cannot be empty!")
        return redirect(url_for('index'))
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
        connection.commit()
        flash("Task added successfully!")
    finally:
        cursor.close()
        connection.close()
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM todos WHERE id = %s", (task_id,))
        connection.commit()
        flash("Task deleted successfully!")
    finally:
        cursor.close()
        connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
