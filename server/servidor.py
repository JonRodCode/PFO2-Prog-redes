from flask import Flask
from routes.usuarioRoutes import usuario_bp
from models.usuarioModel import Usuario

app = Flask(__name__)
app.secret_key = "clave_secreta"

Usuario.crear_tabla()
app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug=True)