from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class ToTest(TestCase):
    def test_home_page(self):
        url=reverse("snack_list")
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_base_page(self):
        url=reverse("snack_list")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"base.html")

    def test_snack_list_page(self):
        url=reverse("snack_list")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"snack_list.html")