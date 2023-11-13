# tests/test_app.py

import os
import openpyxl
import sys
import random
sys.path.append('.')
from app import app, read_categortys, read_products, write_categortys, write_products
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_read_categortys():
    # Tạo một bảng tính Excel với dữ liệu kiểm thử
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'categorty'
    worksheet.append(['id', 'name'])
    worksheet.append([1, 'Category 1'])
    worksheet.append([2, 'Category 2'])
    random_suffix = str(random.randint(0, 999)).zfill(3)
    temp_data_file = f'data/data_test_{random_suffix}.xlsx'
    workbook.save(temp_data_file)

    # Kiểm tra hàm đọc categortys
    categortys = read_categortys()
    assert len(categortys) == 2
    assert categortys[0]['name'] == 'Category 1'
    assert categortys[1]['id'] == 2

    # Đặt đường dẫn tệp dữ liệu tạm thời
    os.rename(temp_data_file, 'data/data_test.xlsx')

def test_read_products():
    # Tạo một bảng tính Excel với dữ liệu kiểm thử
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'products'
    worksheet.append(['id', 'image', 'key', 'name', 'categorty', 'unit', 'quantity'])
    worksheet.append([1, 'image1.jpg', 'key1', 'Product 1', 'Category 1', 'unit1', 10])
    worksheet.append([2, 'image2.jpg', 'key2', 'Product 2', 'Category 2', 'unit2', 20])
    random_suffix = str(random.randint(0, 999)).zfill(3)
    temp_data_file = f'data/data_test_{random_suffix}.xlsx'
    workbook.save(temp_data_file)

    # Kiểm tra hàm đọc products
    products = read_products()
    assert len(products) == 2
    assert products[0]['name'] == 'Product 1'
    assert products[1]['quantity'] == 20

    # Đặt đường dẫn tệp dữ liệu tạm thời
    os.rename(temp_data_file, 'data/data_test.xlsx')


# Tương tự, bạn có thể viết các bài kiểm thử cho các hàm khác như write_categortys, write_products, add_product, edit_product, delete_product, và các hàm khác.
