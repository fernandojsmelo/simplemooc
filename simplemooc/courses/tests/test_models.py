from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

from model_mommy import mommy

from simplemooc.courses.models import Course

class CourseManagerTestCase(TestCase):

    def setUp(self):
        self.courses = mommy.make('courses.Course', name='Python na Web com Django', _quantity=10)
        self.client = Client()

    def tearDown(self):
        for course in self.courses:
            course.delete()

    def test_course_search(self):
        search = Course.object.search('django')
        self.assertEquals(len(search), 10)