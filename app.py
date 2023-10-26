from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    user_data = {
        "name": name,
        "email": email
    }

    # Insert data into MongoDB
    collection.insert_one(user_data)

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
