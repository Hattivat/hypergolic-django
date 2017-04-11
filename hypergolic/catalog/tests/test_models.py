from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from catalog.models import Role


class RoleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.myuser = User.objects.create_user(username='testuser',
                                              password='ytrewq')
        Role.objects.create(name='aaa', description='loremipsum', sources='xx')

    def test_verbose_name(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester._meta.verbose_name, 'Engine role')

    def test_verbose_plural(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester._meta.verbose_name_plural, 'Engine roles')

    def test_get_absolute_url(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester.get_absolute_url(),
                          '/engine_roles/aaa/')

    def test_get_create_url(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester.get_create_url(),
                          '/engine_roles/create/')

    def test_get_update_url(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester.get_update_url(),
                          '/engine_roles/aaa/update/')

    def test_get_delete_url(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester.get_delete_url(),
                          '/engine_roles/aaa/delete/')

    def test_get_list_url(self):
        tester = Role.objects.get(name='aaa')
        self.assertEquals(tester.get_list_url(),
                          '/engine_roles/')