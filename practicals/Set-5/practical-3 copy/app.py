from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

# Set up Flask-JWT-Extended
app.config["JWT_SECRET_KEY"] = ""  # Replace with yoursecret key

jwt = JWTManager(app)
# Dummy user data (replace with a proper user database in a realapplication)

users = {"abc": {"password": "123"}, "def": {"password": "456"}}

# Route to generate a JWT token upon login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username]['password'] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    
# Protected route that requires a valid JWT token for access
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = jwt.get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)