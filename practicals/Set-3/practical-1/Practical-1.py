from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the root URL "/"
@app.route("/")
def home():
    # Render the static HTML page located in the "templates" folder
    return render_template("index.html")

# Run the app if this script is the main program
if __name__ == "__main__":
    app.run(debug=True)
