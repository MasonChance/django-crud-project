from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Snack

# Create your tests here.

class TestSnacks(TestCase):

    def setUp(self):
        # creates a test user and test model much like a fixture in pytest
        self.user = get_user_model().objects.create_user(
            username='tester', email='tester@email.com', password='pass',
        )

        self.snack = Snack.objects.create(
            title='HotPocket', description='Lava Hot or Ice Cold', purchaser=self.user,
        )


    def test_str_rep(self):
        self.assertEqual(self.snack.__str__(),
                'Found HotPocket on tester\'s list because Lava Hot or Ice Cold'
                )


    def test_snack_content(self):
        self.assertEqual(f'{self.snack.title}', 'HotPocket')
        self.assertEqual(f'{self.snack.description}', 'Lava Hot or Ice Cold')
        self.assertEqual(f'{self.snack.purchaser}', 'tester')


    def test_snack_list_view(self):
        # Assign test HTTP request to response variable to mock return
        response = self.client.get(reverse('snack_list'))
        # assertEqual check the status code
        self.assertEqual(response.status_code, 200)
        # assertContains checks response for the second argument passed, 
        # ??? what is it actuall checking? all properties? all content? 
        # can this be manipulated to check for something more specific?
        # is it dependent on how the Model and View are Structured???
        self.assertContains(response, 'HotPocket')
        # assert TemplateUsed checks that the correct filename is referenced
        # by the Mock HTTP request and is returned in the response
        self.assertTemplateUsed(response, 'snack_list.html')
    

    def test_snack_detail_view(self):
        # Mocks HTTP request. ?? what does kwarg: args=1 do????
        response = self.client.get(reverse('snack_detail'))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'title: HotPocket')
        self.assertContains(response, 'description: Lava Hot or Ice Cold')
        self.assertContains(response, 'purchaser: tester')
        self.assertTemplateUsed(response, 'snack_detail.html')


    
