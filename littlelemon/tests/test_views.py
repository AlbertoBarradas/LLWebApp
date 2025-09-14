from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="Soup", price= 15.00, inventory=9)
        item = Menu.objects.create(title="Ice Cream", price= 4.00, inventory=4)

    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
