from flask import Blueprint
from controllers.usuarioController import registro, login, tareas

usuario_bp = Blueprint('usuario', __name__)

usuario_bp.route('/registro', methods=['POST'])(registro)
usuario_bp.route('/login', methods=['POST'])(login)
usuario_bp.route('/tareas', methods=['GET'])(tareas)