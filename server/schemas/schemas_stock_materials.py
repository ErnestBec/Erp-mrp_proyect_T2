def type_stock(type_stock):
    return {
        "_id": str(type_stock["_id"]),
        "name_type": type_stock["name_type"]
    }


def types_stocks(types_stocks):
    return [type_stock(type) for type in types_stocks]


def stock_product(stock_product):
    return {
        "_id": str(stock_product["_id"]),
        "id_type_stock": str(stock_product["id_type_stock"]),
        "name_stock": stock_product["name_stock"],
        "date_update": stock_product["date_update"]
    }


def stocks_products(stock_products):
    return [stock_product(stock) for stock in stock_products]


def rack_stock(rack):
    return {
        "_id": str(rack["_id"]),
        "id_stock": str(rack["id_stock"]),
        "name_rack": rack["name_rack"],
        "width_capacity": rack["width_capacity"],
        "high_capacity": rack["high_capacity"],
        "long_capacity": rack["long_capacity"],
        "date_update": rack["date_update"]
    }


def racks_stock(racks):
    return [rack_stock(rack) for rack in racks]


def floor_rack(floor):
    return {
        "_id": str(floor["_id"]),
        "id_rack": floor["id_rack"],
    }


def floors_rack(floors):
    return [floor_rack(floor) for floor in floors]


def row_rack(row):
    return {
        "_id": str(row["_id"]),
        "id_floor": row["id_floor"],
        "no_row": row["no_row"]
    }


def rows_rack(rows):
    return [row_rack(row) for row in rows]


def space_row(space):
    return {
        "_id": str(space["_id"]),
        "id_row": str(space["id_row"]),
        "id_prod_pz": str(space["id_prod_pz"]),
        "id_stock":str(space["id_stock"]),
        "id_rack":str(space["id_rack"]),
        "status": space["status"]
    }


def spaces_row(spaces):
    return [space_row(space) for space in spaces]
