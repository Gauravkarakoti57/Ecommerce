from unittest import skip
from django.http import response

from django.test import TestCase
from django.http import HttpRequest
from store.views import all_products
from django.contrib.auth.models import User
from store.models import Category, Product
from  django.urls import reverse
from django.test import Client


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse("store:product_detail", args=["django-beginners"]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>',html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
    