from django.test import TestCase
from django.urls import reverse


class PrivacyPagesTests(TestCase):
    def test_privacy_policy_is_public_and_returns_200(self):
        response = self.client.get(reverse("politica-de-privacidade"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Política de Privacidade")
        self.assertContains(response, "62.391.324/0001-55")
        self.assertContains(response, 'name="robots" content="index, follow"')
        self.assertContains(response, "https://gestcloud.com.br/politica-de-privacidade/")

    def test_data_deletion_is_public_and_returns_200(self):
        response = self.client.get(reverse("exclusao-de-dados"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Exclusão de dados")
        self.assertContains(response, "contact@gestcloud.com.br")
        self.assertContains(response, "https://gestcloud.com.br/exclusao-de-dados/")

    def test_home_footer_links_to_legal_pages(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("politica-de-privacidade"))
        self.assertContains(response, reverse("exclusao-de-dados"))
