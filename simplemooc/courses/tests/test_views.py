from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

from simplemooc.courses.models import Course

class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.course = Course.object.create(name='Django', slug='django')

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name': 'Fulano de Tal', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        #self.assertFormError(response, 'form', 'email', 'Este campo é Obrigadório.')
        #self.assertFormError(response, 'form', 'message', 'Este campo é Obrigadório.')

    def test_contact_form_success(self):
        data = {'name': 'Fulano de Tal', 'email': 'admin@admin.com', 'message': 'Oi'}
        client = Client()
        path = reverse( 'courses:details', args=[self.course.slug] )
        response = client.post( path, data )
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].to, [settings.CONTACT_EMAIL])