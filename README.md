# Sistema de Gestión de Tareas con API y Base de Datos 

## Instalación

1. Clonar o descargar el proyecto
2. Instalar dependencias. Ejecutar en la terminal:   
```bash
pip install flask requests
```

## Ejecución del servidor

1. En la terminal, navegar a la carpeta server con:
```bash
  cd server
```
2. Ejecutar:
```bash
   python servidor.py
```

## Ejecución del cliente

1. Abrir una nueva terminal, navegar a la carpeta client con:
```bash
   cd client
```
2. Ejecutar:
```bash
  python cliente.py
```

## Pruebas del cliente y servidor

1. En el cliente se encontrará un menú de opciones.

<img width="556" height="136" alt="Captura de pantalla 2026-05-04 200647" src="https://github.com/user-attachments/assets/bba70777-30bb-4d5f-a226-f5d9a30341ad" />

2. Elegir opcion 1 y completar los campos solicitados para el registro

<img width="551" height="124" alt="Captura de pantalla 2026-05-04 200748" src="https://github.com/user-attachments/assets/99f9322c-f73a-4252-9def-49cf3e733d41" />

3. Luego elegir opcion 2 y completar los campos solicitados para el login

<img width="546" height="77" alt="Captura de pantalla 2026-05-04 200941" src="https://github.com/user-attachments/assets/e301655c-f266-41d2-adb1-908ce3dd6bbd" />

4. Lo siguiente seria elegir la opcion 3 para ver el mensaje de bienvenida

<img width="532" height="90" alt="Captura de pantalla 2026-05-04 201624" src="https://github.com/user-attachments/assets/cb1d2917-ac84-4a96-9174-c36a008fab50" />

5. Extra: corroboración de usuario con contraseña hasheada

<img width="650" height="127" alt="Captura de pantalla 2026-05-04 201915" src="https://github.com/user-attachments/assets/cf0b543b-f9c9-475e-87d8-cf23882bfb17" />

## ¿Por qué hashear contraseñas?

Es importante hashear las contraseñas para no almacenarlas en texto plano. De esta forma, aunque alguien acceda a la base de datos, no podrá ver las contraseñas reales de los usuarios, lo que aumenta significativamente la seguridad.

## Ventajas de usar SQLite en este proyecto

Es simple de usar, no requiere instalación adicional y funciona con un solo archivo. Es ideal para aplicaciones pequeñas porque reduce la configuración necesaria para probar el sistema.
