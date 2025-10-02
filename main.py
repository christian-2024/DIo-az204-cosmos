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



database = create_database()