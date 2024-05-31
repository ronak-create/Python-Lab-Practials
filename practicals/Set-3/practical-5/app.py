from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        # Get user input from the form
        user_input = request.form.get('user_input')

        # Process the input (you can replace this with your processing logic)
        result = f"You entered: {user_input}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
