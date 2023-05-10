from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import csv

class Marca(str, Enum):
    audi = 'Audi' 
    bmw = 'BMW' 
    chery = 'Chery' 
    chevrolet = 'Chevrolet' 
    chrysler = 'Chrysler' 
    citroen = 'Citroen' 
    dodge = 'Dodge' 
    fiat = 'Fiat' 
    ford = 'Ford' 
    geely = 'Geely' 
    honda = 'Honda' 
    hyundai = 'Hyundai' 
    jac = 'JAC' 
    jeep = 'Jeep' 
    kia = 'Kia' 
    lexus = 'Lexus' 
    lifan = 'Lifan' 
    mercedes = 'Mercedes-Benz' 
    mini = 'Mini' 
    mitsubishi = 'Mitsubishi' 
    nissan = 'Nissan' 
    porsche = 'Porsche' 
    ram ='RAM' 
    renault = 'Renault' 
    smart = 'Smart' 
    ssangyong = 'Ssangyong' 
    subaru = 'Subaru' 
    suzuki = 'Suzuki' 
    tesla = 'Tesla' 
    toyota = 'Toyota' 
    volkswagen = 'Volkswagen' 
    volvo = 'Volvo'
        
    
class Portas(str, Enum):
   duas = 2
   quatro = 4

class Transmissao(str, Enum):
    automatica = 'automatica'
    manual = 'manual'
    semiautomatica = 'semiautomatica'

class Direcao(str, Enum):
    mecanica = 'mecanica'
    hidraulica = 'hidraulica'
    eletrica = 'eletrica'

class Combustivel(str, Enum):
    gasolina = 'gasolina'
    etanol = 'etanol'
    flex = 'flex'
    diesel = 'diesel'
    eletricidade = 'eletricidade'

class Carroceria(str, Enum):
    sedan = 'sedan'
    hatch = 'hatch'
    SUV = 'SUV'
    pickup = 'pickup'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    marca: List[Marca]
    modelo: str
    ano: int
    versao: float
    portas: List[Portas]
    transmissao: List[Transmissao]
    direcao: List[Direcao]
    combustivel: List[Combustivel]
    carroceria: List[Carroceria]
    
    @classmethod
    def from_csv(cls, filename: str) -> List['User']:
        with open('vehicles.csv', 'r') as file:
            reader = csv.DictReader(file)
            users = []
            for row in reader:
                ano = datetime.strptime(row['ano'], '%Y').year    
                user = cls(
                    marca=[Marca(m) for m in row['marca'].split(';')],
                    modelo=row['modelo'],
                    ano=ano,
                    versao=float(row['versao']),
                    portas=[Portas(p) for p in row['portas'].split(';')],
                    transmissao=[Transmissao(t) for t in row['transmissao'].split(';')],
                    direcao=[Direcao(d) for d in row['direcao'].split(';')],
                    combustivel=[Combustivel(c) for c in row['combustivel'].split(';')],
                    carroceria=[Carroceria(car) for car in row['carroceria'].split(';')]
                )
                users.append(user)
        return users
    