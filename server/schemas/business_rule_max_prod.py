# Los esquemas son la estructura en que se retornan las respuestas al usuario, esto con el fin de regresarlos en formato de objetos para despues manejarlos como tipo json, ademas que nos sirve para la documentacion de fastApi, esto es para todos los archivos que estan en la carpeta de esquemas, dichos esquemas los datos a los que accede como tipo objeto deben de ser los mismos que estan en la base de datos  

# retorna solo un objeto, este se usa para cuando solo tienes que retornar una respuesta al ususario de un solo objeto, en este caso retorna un solo objeto de las reglas de produccion, recibe un parametro y retorna dichjo parametro como tipo objeto, pueden ser datos de la bd  
def business_rule_schema(business_rule) -> dict:
    return {
        "_id": str(business_rule["_id"]),
        "max_pro": business_rule["max_prod"],
        "min_prod": business_rule["min_prod"]
    }

# retorna una lista de objetos, este se usa para cuando solo tienes que retornar una respuesta al ususario de una lista de  objetos, en este caso retorna una lista de  objetos de las reglas de produccion, recorre la lista pasada por parametro y cada iteracion la convierte a tipo objeto para poder retornar una lista de objetos
def busness_rules_schema(business_rules) -> list:
    return [business_rule_schema(rule) for rule in business_rules]
