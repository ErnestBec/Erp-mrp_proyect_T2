# Esta parte es el ruteo de nuestra aplicacion, aqui definimos los endpoints para cada entidad de la base de datos, esta parte es importante ya que nos permite la conexion con el cliente aqui es en donde le solicitamos al cliente la estructura en que necesitamos los datos que ingresara, esto es lo mismo para cada archivo de la carpeta routes

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from utils.db import db_name
# Schemas
from schemas.business_rule_max_prod import busness_rules_schema
# Models
from models.business_rule_models import BusinnesRuleMaxProd
# Middlewares
from middlewares.auth_middleware import  protectedAcountAdmin,Portador
# Controllers
from controllers.business_rules_controller import new_business_rule_prod_capacity, update_busimess_rule_prod_capacity

# inicializamos una nueva instancia de APIRouter, dicha instancia contendra todas las riutas que necesitemos para cada entidad de la bd
# Routing request
routes_business_rules = APIRouter()


# Routes Business Rules Production Capacity


# Decoramos la instancia antes creada seguido del metodo que utilizzara ya sea POST,DELETE, PUT, PATCH, seguido de la ruta fica por donde ingresara al endpoint, en este caso es '/admin/new_rule/production_capacity', el atributo target es para Seccionar nuestras rutas en este casi cada ruta de este archivo entrara en la seecion de Petition Rules.


# New Business Rule Production Capacity
# Aqui en en donde se utiliza tambien la proteccion de rutas con el uso de los middlewares, si el midleware retorna parametros se tiene que ingresar como atributo dentro de la funcion que decora el endpoint, y si no retorna valor se coloca en seguida de la ruta del endpoint en un atributo llamado dependences= dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())], que es un arreglo de dependencia que usaran los middlewares
@routes_business_rules.post("/admin/new_rule/production_capacity", tags=["Petition Rules"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
# Las funciones que que van despues del decorador, son las que recibiran los parmetros ingresados por el ususario, en este caso esta funcion recibe el parametro de business_rule, dicho parametro es de tipo BusinnesRuleMaxProd que el modelo que recibe la bd
def new_business_rule_prod_capacity_route(business_rule: BusinnesRuleMaxProd):
    # en este caso se envian los datos ingresados por el usuario al controlador correspondiente, es quien hace la logica del negocio para retornar  o no valores al cliente o a la bd
    return new_business_rule_prod_capacity(business_rule)

# Get Rule Production Capacity

# los middlewares se ejecutan en seguida de que se envian los datos del cliente, si cumple con las condiciones especificadas en el middleware se sigue la ejecucion si no retorna mensaje al cliente
@routes_business_rules.get("/admin/get_rule/production_capacity" , tags=["Petition Rules"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
def get_rule_prod_capacity_route():
    business_rule = db_name.BusinessRuleMaxProd.find()
    # en este caso se retotna una lista de objetos, por ello se le pasa la lista que retorna la bd y se envia a el schema que hacer la conversion correspondiente
    return JSONResponse(content={"Business Rules": busness_rules_schema(business_rule)}, status_code=200)


# Update Business Rule Production Capacity


@routes_business_rules.patch("/admin/update_rule/production_capacity" , tags=["Petition Rules"], dependencies=[Depends(Portador()),Depends(protectedAcountAdmin())])
def update_rule_prod_capacity_route(business_rule: BusinnesRuleMaxProd):
    return update_busimess_rule_prod_capacity(business_rule)
