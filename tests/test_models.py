from ..models import Answer
from django.contrib.auth.models import User
from django.test import TestCase

class AnswerTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user('test', 'test@test.com', 'test')
		Answer.objects.create(result=True, user=self.user)
		Answer.objects.create(result=False, user=self.user)

	def test_manager(self):
		objects = Answer.objects.for_user(self.user)
		results = [result.result for result in objects]
		self.assertEqual(2, len(objects))
		self.assertTrue(True in results)
		self.assertTrue(False in results)

