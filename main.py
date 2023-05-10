
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from models import User, Marca, Portas, Transmissao, Direcao, Combustivel, Carroceria
import csv

app = FastAPI()

def read_csv(filename: str) -> List[User]:
    with open('vehicles.csv', 'r') as file:
        reader = csv.DictReader(file)
        users = []
        for row in reader:
            user = User(
                id=uuid4(),
                marca=[Marca(m) for m in row['marca'].split(';')],
                modelo=row['modelo'],
                ano=int(row['ano']),
                versao=float(row['versao']),
                portas=[Portas(p) for p in row['portas'].split(';')],
                transmissao=[Transmissao(t) for t in row['transmissao'].split(';')],
                direcao=[Direcao(d) for d in row['direcao'].split(';')],
                combustivel=[Combustivel(c) for c in row['combustivel'].split(';')],
                carroceria=[Carroceria(car) for car in row['carroceria'].split(';')]
            )
            users.append(user)
        return users

database: List[User] = read_csv('vehicles.csv')

# @app.get("/")
# async def root():
#     return {'message': 'Its working'}

@app.get("/api/v1/users")
async def fetch_users():
    return database


@app.get("/api/v1/users/modelo")
async def fetch_users(modelo: Optional[str] = None):
    if modelo:
        filtered_users = [user for user in database if user.modelo == modelo]
        return filtered_users
    else:
        return database

@app.post("/api/v1/users")
async def register_users(user: User):
    database.append(user)
    return{"user": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_users(user_id: UUID):
    for user in database:
        if user.id == user_id:
            database.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"Car not found: {user_id}",
    )


