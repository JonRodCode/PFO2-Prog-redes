from flask import request, jsonify, session
from models.usuarioModel import Usuario

def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")
    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400
    if Usuario.crear(usuario, contraseña):
        return jsonify({"mensaje": "Usuario creado"}), 201
    else:
        return jsonify({"error": "Usuario ya existe"}), 400

def login():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")
    user = Usuario.buscar(usuario)
    if user and Usuario.verificar_password(user, contraseña):
        session['usuario'] = usuario
        return jsonify({"mensaje": "Login exitoso"}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

def tareas():
    if 'usuario' not in session:
        return jsonify({"error": "No autorizado"}), 401
    return f"<h1>Bienvenido {session['usuario']}</h1>"