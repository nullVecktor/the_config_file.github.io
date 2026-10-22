#el archivo run.py tiene como misión arrancar el servidor de nuestro CMS.
#no contiene el dashboard ni gestiona los artículos, prepara la aplicación y la pone a funcionar.
#
from app import create_app

app = create_app() 



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)