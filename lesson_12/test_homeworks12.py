import pytest

from lesson_12.previous_homeworks import (
    sum_numbers,
    Rhombus,
    fuel_required,
    tanks_required,
    order_price_calculator
)

# ================= test_function_01 =================
def test_sum_numbers_positive():
    assert sum_numbers("1, 2, 3, 4") == 10

def test_sum_numbers_string_with_letters():
    assert sum_numbers("qwerty1,2,3") == "Не можу це зробити!"

# ================= test_function_02 =================
def test_rhombus_create():
    rhombus = Rhombus(10, 60)
    assert rhombus.side_a == 10
    assert rhombus.corner_a == 60
    assert rhombus.corner_b == 120

def test_rhombus_negative_side():
    with pytest.raises(ValueError):
        Rhombus(-5, 60)

def test_rhombus_invalid_corner():
    with pytest.raises(ValueError):
        Rhombus(10, 180)

def test_rhombus_corner_b_manual_change():
    rhombus = Rhombus(10, 60)
    with pytest.raises(AttributeError):
        rhombus.corner_b = 90

# ================= test_function_03 =================
def test_fuel_required_rounds_up_full_litre():
    assert fuel_required(1599, 100, 9) == 144

def test_tanks_required():
    assert tanks_required(100, 50) == 2

# ================= test_function_04 =================
def test_order_price_calculator():
    items = [
        ("Pizza", 2, 100),
        ("Juice", 3, 20)
    ]
    assert order_price_calculator(items) == 260

def test_order_price_empty_list():
    assert order_price_calculator([]) == 0