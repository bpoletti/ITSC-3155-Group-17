import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


# @pytest.fixture()
# def input_value():
#   input_value = {'y', 'n'}
#  return input_value


def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurPrice(products)
    assert invoice.totalPurPrice(products) == 69.38


def test_canAddPrice():
    assert Invoice.addPrice(1, 2) == 3

# def test_CanInputNumber(invoice):
#   val = invoice.inputNumber(input_value=5)
#  assert not val
