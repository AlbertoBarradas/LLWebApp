from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Hamburguer", price= 30.00, inventory=10)
        self.assertEqual(item.title, "Hamburguer")
        self.assertEqual(str(item.price), "30.0")
        self.assertEqual(str(item.inventory), "10")