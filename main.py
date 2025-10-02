from azure.cosmos import CosmosClient, PartitionKey, exceptions
from dotenv import load_dotenv
import os
load_dotenv()

URL = os.getenv("URL")
KEY = os.getenv("KEY")
DATABASE = os.getenv("DATABASE")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

client = CosmosClient(URL, KEY)  

#Criar um banco de dados

def create_database():
    try:
        database = client.create_database(id=DATABASE)
        print(f"Database '{database.id}' criado com sucesso ")
    except exceptions.CosmosResourceExistsError:
        database = client.get_database_client(DATABASE)
        print(f"Banco de dados '{DATABASE}' já existe.")
    return database

#Criar um contêiner
def create_container(database):
    try:
        container = database.create_container(id=CONTAINER_NAME, partition_key=PartitionKey(path="/id"))
        print(f"O contêiner '{container.id}' criado com sucesso ")
    except exceptions.CosmosResourceExistsError:
        container = database.get_container_client(CONTAINER_NAME)
        print(f"O contêiner '{CONTAINER_NAME}'já existe.")
    return container

#Criar item no contêiner
def create_item(container):
    item = {
        "id": "2",
        "ProductID": "1",
        "ProductName": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "price": 9.99
    }

    container.create_item(body=item)
    print("Iterm criado com sucesso!")


database = create_database()
container = create_container(database)
create_item(container)