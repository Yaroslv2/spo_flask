from flask import Blueprint, jsonify, request
from services.auth import find_user_by_login

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

def func():
    return 1, 2, 3, 4

a, b, c, d = func()

@auth_bp.route("/login", methods=["POST"])
def login():
    # if silent = True return None
    data = request.get_json(silent=False)

    # Если тип данных переменной data не является dict (то есть словарь), 
    # сделать какое-то действие
    if not isinstance(data, dict):
        # Вернуть JSON и статус код 400
        return jsonify({"error": "Expected a JSON object"}), 400

    # Получаем значения из data
    login = data.get("login")
    password = data.get("password")

    # Проверяем, что данные вообще есть, которые ожидаются в теле запроса
    if not login or password is None:
        # Возвращаем ошибку, если каких-то данных не хватает
        return jsonify({"error": "login and password is required"}), 400

    # БИЗНЕС-ЛОГИКА
    user = find_user_by_login(login, password)
    if user is None:
        return jsonify({"error": "user with that credentials is not found"}), 404
    
    return jsonify({"user": user})
