from django.test import TestCase
from decimal import Decimal
from catalog.helpers import strip_mid_whitespace
from catalog.models import Role, Compound, PropellantMix


class RoleModelTest(TestCase):
    """Since Role inherits almost all of its logic from the Basic model,
    this is assumed to test not just Role, but all other models which inherit
    from Basic without significantly extending it."""

    @classmethod
    def setUpTestData(cls):
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


class PropellantMixModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        hydra = Compound.objects.create(name='hydrazine', role=True,
                                        sources='xx')
        hydra.save()
        tetro = Compound.objects.create(name='nitrogen tetroxide', role=False,
                                        sources='xx')
        tetro.save()
        themix = PropellantMix.objects.create(hypergolic=True,
                                              specific_impulse=3500,
                                              combustion_temp=Decimal(3250),
                                              sources='xx')
        themix.save()
        themix.propellants = [hydra, tetro]

    def test_verbose_plural(self):
        tester = PropellantMix.objects.get(pk=1)
        self.assertEquals(tester._meta.verbose_name_plural, 'Propellant mixes')

    def test_combustion_temp_verbose(self):
        tester = PropellantMix.objects.get(pk=1)
        verbal = tester._meta.get_field('combustion_temp').verbose_name
        verbal = strip_mid_whitespace(verbal)
        self.assertEquals('combustion temperature', verbal)

    def test_specific_impulse_verbose(self):
        tester = PropellantMix.objects.get(pk=1)
        verbal = tester._meta.get_field('specific_impulse').verbose_name
        verbal = strip_mid_whitespace(verbal)
        self.assertEquals('Specific impulse in vacuum', verbal)

    def test_str(self):
        tester = PropellantMix.objects.get(pk=1)
        self.assertEquals(tester.__str__(), 'hydrazine/nitrogen tetroxide')
