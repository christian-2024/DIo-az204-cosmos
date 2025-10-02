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
def create_item(container, item):
    

    container.create_item(body=item)
    print("Iterm criado com sucesso!")

#Realizar Update Item

def update_item(container):
    item = container.read_item(item="1", partition_key="1")
    item["price"] = 19.99
    container.upsert_item(body=item)
    print("Item atualizado com sucesso!")

#Realizar delete de Itens
def delete_item(container):
    container.delete_item(item="1", partition_key="1")
    print("Item excluído com sucesso!")

#Lendo todos os Items
def read_items(container):
    items = container.read_all_items()
    for item in items:
        print(item)  

#Lei item pelo ID
def read_item(container):
    item = container.read_item(item="2", partition_key="1")
    print(item)          

if __name__ == "__main__":
    database = create_database()
    container = create_container(database)

item = {
        "id": "3",
        "ProductID": "1",
        "ProductName": "Senhor dos Aneis",
        "author": "Não encontrado",
        "price": 19.99
    }    

#create_item(container, item)
#update_item(container)
#delete_item(container)
#read_items(container)
read_item(container)