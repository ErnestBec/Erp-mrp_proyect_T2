def productEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "Descripcion": item["Descripcion"],
        "min_stock": item["min_stock"],
        "max_stock": item["max_stock"],
        "precio_uni": item["precio_uni"],
        "num_pieza": item["num_pieza"],
        "category_prod": item["category_prod"],
        "cantidad_prod": item["catindad_prod"],
        "mp":item[{
            "tipo":item["tipo"],
            "quantity":item["quantity"]
        }
        ],
        "lote_prod": [{
            "fecha":item["fecha"],
            "mat_pro":item["mat_prod"]
        }
        ],
        "lote_Almacen": [{
            "tipo":item["tipo"],
            "quantity":item["quantity"],
            "piso":[{
                "num_piso":item["num_piso"],
                "num_fila":item["num_fila"],
                "rack":[{
                    "capacidad": item["capacidad"],
                    "num_espcacio": item["num_espacio"]
                }]

            }]

        }
        ]


    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
