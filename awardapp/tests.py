from django.test import TestCase
from .models import *

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='Steve')
        self.profile = Profile.objects.create(user = self.user,bio = 'loves coding', contact='0745697834')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_all_profiles(self):
        self.profile.save()
        profile = Profile.get_all_profiles()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('Steve')
        self.assertTrue(len(profile) > 0)
