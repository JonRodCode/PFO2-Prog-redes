import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DB_NAME = "usuarios.db"

class Usuario:

    @staticmethod
    def crear_tabla():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contraseña TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def crear(usuario, contraseña):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        hash_pass = generate_password_hash(contraseña)

        try:
            cursor.execute(
                "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
                (usuario, hash_pass)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @staticmethod
    def buscar(usuario):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = ?",
            (usuario,)
        )
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def verificar_password(user, contraseña):
        return check_password_hash(user[2], contraseña)