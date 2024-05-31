from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

# Configure the SQLAlchemy database URI. Here, we're using SQLite for simplicity.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance
db = SQLAlchemy(app)

# Define a model for the data
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Sample data for demonstration
sample_data = [{'name': 'John', 'age': 25},
               {'name': 'Alice', 'age': 30},
               {'name': 'Bob', 'age': 22}]

# Populate the database with sample data
with app.app_context():
    db.create_all()
    for entry in sample_data:
        person = Person(name=entry['name'], age=entry['age'])
        db.session.add(person)
    db.session.commit()

# Define a route to display data in tabular format
@app.route('/')
def display_data():
    # Query data from the database
    data = Person.query.all()

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame([(person.name, person.age) for person in data], columns=['name', 'age'])

    # Convert the DataFrame to HTML for rendering in the template
    table_html = df.to_html(classes='table table-striped', index=False)

    return render_template('index.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)