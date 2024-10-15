from django.test import TestCase
from Restaurant.models import *
from Restaurant.serializers import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = 'Ice Cream',Price = 80,Inventory = 100)
        self.assertEqual(str(item),"Ice Cream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(Id=2,Title = 'Chocolate Cream',Price = 100 ,Inventory = 80)
    
    def test_getall(self):
        self.item = Menu.objects.all()
        serialized_item = MenuSerializer(self.item,many = True)
        self.assertEqual (serialized_item.data,[
            {"Id":int(serialized_item.data[0]['Id']), "Title" : "Chocolate Cream", "Price" : '100.00' ,"Inventory": 80}
        ])
# [{'Id': 2, 'Title': 'Chocolate Cream', 'Price': '100.00', 'Inventory': 80}]
# [{'Id': 2, 'Title': 'Chocolate Cream', 'Price': '100.00', 'Inventory': 80}]
# [{'Id': 2, 'Title': 'Chocolate Cream', 'Price': 100.0, 'Inventory': 80}]