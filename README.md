# BMXAPIDataVisualization

This repo contains a web application to obtain the values of UDIS and USD by querying the API
[BMXApi](https://www.banxico.org.mx/SieAPIRest/service/v1/;jsessionid=5fa4f900baccc38cd60cb4f38981).  It shows the values from the selected  date range including a graph, an average value, minimum value and a maximum value in the date range.


## Setup &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-397/)

- Set up and activate the local development environment.


- Install the requirements using pip:

    ```sh
    pip install -r requirements.txt
    ```

- Setup local MySql database and use django migrations 

    ```sh
    python Pokemon/manage.py makemigrations
    python Pokemon/manage.py migrate
    # This will setup the local database based on django models. Make sure you are in the same directory as manage.py file
    ```
- Run the server as follows:

    ```sh
    python currAPI/manage.py runserver
    ```

- If your development server is at localhost then you can access the api by using:

http://127.0.0.1:8000/

or

http://127.0.0.1:8000/
