from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

# Create your testes here.
from simplemooc.courses.models import Course

class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.object.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name':'Fulano de Tal', 'email': '', 'message':''}
        client = Client()
        path = reverse('course:details', args=[self.course.slug])
        response = client.post(path)
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório')

    def test_contact_form_success(self):
        data = {'name': 'Fulano de Tal', 'email': 'admin@admin.com', 'message': 'oi'}
        client = Client()
        path = reverse( 'course:details', args=[self.course.slug] )
        response = client.post( path )
        self.assertEquals(len(mail.outbox), 1)