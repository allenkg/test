import pytest

from products.models import Product

URL = '/v1/products/'

@pytest.mark.django_db
def test_fetch_products(client, initialize_test_data):
    response = client.get(URL)
    assert len(response.data['results']) == 10
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_product_qty(client, initialize_test_data, user_factory):
    user = user_factory.create(email='test@product.com')
    client.force_authenticate(user)
    product = Product.objects.all().first()
    old_qty = product.qty
    response = client.patch(f"{URL}{product.id}/", {"qty": 5})
    product.refresh_from_db()

    assert str(old_qty) != response.data['qty']
    assert response.status_code == 200


