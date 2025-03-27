import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from dashboard.models import Product, Order

# ========================== BDD (Behavior-Driven Development) ==========================
# BDD se centra en describir el comportamiento del sistema en términos de negocio.
# Usamos nombres descriptivos y pruebas que reflejan casos de uso reales.
# Se espera que las pruebas sean comprensibles incluso para personas no técnicas.

@pytest.fixture
def user(db):
    """Fixture para crear un usuario en la base de datos de prueba."""
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def client_logged_in(client, user):
    """Fixture para autenticar un usuario antes de ejecutar los tests."""
    client.login(username='testuser', password='testpass')
    return client

# ========================== TDD (Test-Driven Development) ==========================
# Se escriben pruebas para verificar el comportamiento del sistema antes de implementar funcionalidades.

@pytest.mark.django_db
def test_index_view(client_logged_in):
    """Prueba para verificar que la vista del dashboard carga correctamente."""
    response = client_logged_in.get(reverse('dashboard-index'))
    assert response.status_code == 200  # Se espera un código 200 (OK)
    assert 'orders' in response.context  # Verifica que la plantilla recibe 'orders'
    assert 'products' in response.context  # Verifica que la plantilla recibe 'products'

@pytest.mark.django_db
def test_staff_view(client_logged_in):
    """Prueba para verificar que la vista de staff carga correctamente."""
    response = client_logged_in.get(reverse('dashboard-staff'))
    assert response.status_code == 200
    assert 'workers' in response.context  # Verifica que la plantilla recibe 'workers'

@pytest.mark.django_db
def test_product_view(client_logged_in):
    """Prueba para verificar que la vista de productos carga correctamente."""
    response = client_logged_in.get(reverse('dashboard-product'))
    assert response.status_code == 200
    assert 'items' in response.context  # Verifica que la plantilla recibe 'items'

'''
@pytest.mark.django_db
def test_product_creation(client_logged_in):
    """Prueba para verificar la creación de productos."""
    product_data = {'name': 'Laptop', 'price': 1000}
    response = client_logged_in.post(reverse('dashboard-product'), data=product_data)
    assert response.status_code == 302  # Se espera una redirección tras la creación
    assert Product.objects.count() == 1  # Verifica que el producto se haya creado
    assert Product.objects.first().name == 'Laptop'  # Verifica que el nombre sea correcto
'''

@pytest.mark.django_db
def test_product_delete(client_logged_in):
    """Prueba para verificar que un producto puede ser eliminado."""
    product = Product.objects.create(name='Mouse', price=50)  # Se crea un producto de prueba
    response = client_logged_in.post(reverse('dashboard-product-delete', args=[product.id]))
    assert response.status_code == 302  # Se espera una redirección tras eliminar el producto
    assert Product.objects.count() == 0  # Se verifica que el producto ya no exista en la BD

@pytest.mark.django_db
def test_order_view(client_logged_in):
    """Prueba para verificar que la vista de pedidos carga correctamente."""
    response = client_logged_in.get(reverse('dashboard-order'))
    assert response.status_code == 200
    assert 'orders' in response.context  # Verifica que la plantilla recibe 'orders'
