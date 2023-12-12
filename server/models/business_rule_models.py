from typing import Optional
from pydantic import BaseModel
# Cada archivo en esta carpeta de modelos, contiene los modelos en que se reciben los datos de parte del cliente, dichos modelos tienen que ser iguales a los que tiene la bd, esto para mantener un estandar en las inserciones de la base de datos, son de tipo BaseModel, cada atributo de la clase se define el tipo de datos que ingresara el ususario

class BusinnesRuleMaxProd(BaseModel):
    _id: Optional[str]
    max_prod: int
    min_prod: int
