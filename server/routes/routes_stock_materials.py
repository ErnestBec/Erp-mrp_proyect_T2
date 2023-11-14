from fastapi import APIRouter, Depends
from utils.db import db_name
from schemas.schemas_stock_materials import floor_stock, floors_rack, rack_stock, racks_stock, row_rack, rows_rack, space_row, spaces_row, stock_product, stocks_products, type_stock, types_stocks
