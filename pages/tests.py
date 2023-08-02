from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('pages:home'))
        self.assertContains(response, 'Home')

    def test_about_us_page_url_by_name(self):
        response = self.client.get(reverse('pages:about_us'))
        self.assertEquals(response.status_code, 200)

    def test_about_us_page_content(self):
        response = self.client.get(reverse('pages:about_us'))
        self.assertContains(response, 'AboutUs')
