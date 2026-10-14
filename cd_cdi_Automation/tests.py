from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeFormTests(TestCase):
    def test_create_form_opens(self):
        for url in [reverse('employee-create-form'), '/employees/create/form/']:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'name="email"')
                self.assertNotContains(response, 'name="date_joined"')

    def test_create_employee_redirects_to_list(self):
        response = self.client.post(reverse('employee-create-form'), {
            'name': 'Test Employee',
            'email': 'employee@example.com',
            'position': 'Developer',
        }, follow=True)
        self.assertRedirects(response, reverse('employee-list-view'))
        self.assertContains(response, 'employee@example.com')
        self.assertIsNotNone(Employee.objects.get().date_joined)

    def test_invalid_form_does_not_create_employee(self):
        response = self.client.post(reverse('employee-create-form'), {
            'name': 'Test Employee',
            'email': 'invalid',
            'position': 'Developer',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', response.context['form'].errors)
        self.assertFalse(Employee.objects.exists())
