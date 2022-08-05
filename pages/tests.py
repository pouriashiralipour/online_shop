from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_url_by_name(self):
        response = self.client.get(reverse('about_page'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home_page'))
        self.assertContains(response, 'HomePage')

    def test_about_page_content(self):
        response = self.client.get(reverse('about_page'))
        self.assertContains(response, 'About US')

    def test_home_page_template_used(self):
        response = self.client.get(reverse('home_page'))
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_template_used(self):
        response = self.client.get(reverse('about_page'))
        self.assertTemplateUsed(response, 'pages/about_us.html')
