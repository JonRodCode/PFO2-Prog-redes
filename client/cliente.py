import requests

BASE_URL = "http://127.0.0.1:5000"

class ClienteAPI:
    def __init__(self):
        self.session = requests.Session()

    def registro(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        res = self.session.post(f"{BASE_URL}/registro", json={
            "usuario": usuario,
            "contraseña": contraseña
        })

        print(res.status_code, res.json())

    def login(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        res = self.session.post(f"{BASE_URL}/login", json={
            "usuario": usuario,
            "contraseña": contraseña
        })

        print(res.status_code, res.json())

    def tareas(self):
        res = self.session.get(f"{BASE_URL}/tareas")

        print("Status:", res.status_code)
        print("Respuesta:")
        print(res.text)

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Registro")
            print("2. Login")
            print("3. Ver tareas")
            print("4. Salir")

            opcion = input("Elegí una opción: ")

            if opcion == "1":
                self.registro()
            elif opcion == "2":
                self.login()
            elif opcion == "3":
                self.tareas()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")


if __name__ == "__main__":
    cliente = ClienteAPI()
    cliente.menu()