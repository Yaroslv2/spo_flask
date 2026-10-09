
from flask import Flask
from routes.users import users_bp
from routes.auth import auth_bp

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return {"message": "API is running"}

if __name__ == "__main__":
    app.run(debug=True) 
