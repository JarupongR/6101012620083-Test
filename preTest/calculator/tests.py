from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from calculator.views import home_page
from calculator.models import History
class HomepageTest(TestCase):

    def test_rootURL_mapping_to_homepageView(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
    
    def test_rendering_homepageTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_calculate_twoNumber_(self):
        response = self.client.post('/', data={'first_number': '12345','second_number' : '12345','operator_type' : '+'})
        self.assertContains(response,'24690.0')
        
    def test_saving_and_verifying_modelItems(self):
        firstCal = History.objects.create(expression= '1+2',answer = '3')
        secondCal = History.objects.create(expression= '5-4',answer = '1')
        
        saved_calculates = History.objects.all()
        self.assertEqual(saved_calculates.count(),2)

        first_saved_calculate = saved_calculates[0]
        second_saved_calculate = saved_calculates[1]

        self.assertEqual(first_saved_calculate.expression,'1+2')
        self.assertEqual(second_saved_calculate.expression,'5-4')
        self.assertEqual(first_saved_calculate.answer,'3')
        self.assertEqual(second_saved_calculate.answer,'1')

    def test_displays_itemInTable(self):
        firstCal = History.objects.create(expression= '1+2',answer = '3')
        secondCal = History.objects.create(expression= '5-4',answer = '1')
        response = self.client.post('/', data={'first_number': '12345','second_number' : '12345','operator_type' : '+'})
        self.assertContains(response,'24690.0')
        self.assertContains(response,'3')
        self.assertContains(response,'1')
