from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    native_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    established = models.DateField(blank=True)
    active = models.BooleanField(blank=True)
    defunct = models.DateField(blank=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)

class Compound(models.Model):
    name = models.CharField(max_lenght=100, primary_key=True, unique=True)
    role = models.BooleanField() # true = fuel, false = oxidizer
    chem_formula = models.CharField(max_length=30)
    density = models.FloatField()
    melting_point = models.DecimalField(max_digits=6, decimal_places=2)
    boiling_point = models.DecimalField(max_digits=6, decimal_places=2)
    appearance = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(max_length=20, blank=True)
    storability = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

class Fuel_Oxidizer_Mix(models.Model):
    fuel = models.ForeignKey(Compound, on_delete=models.CASCADE, limit_choices_to={'role': True})
    oxidizer = models.ForeignKey(Compound, on_delete=models.CASCADE, limit_choices_to={'role': False})
    specific_impulse = models.IntegerField() # stored in m/s
    specific_impulse_sl = models.IntegerField(blank=True) # stored in m/s
    optimum_ratio = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    combustion_temp = models.DecimalField(max_digits=6, decimal_places=1, blank=True)
    description = models.TextField(blank=True)

class Engine(models.Model):
    name = models.CharField(max_length=50)
    variant_of = models.ForeignKey(self, on_delete=models.SET_NULL, blank=True)
    native_name = models.CharField(max_length=50, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    application = models.CharField(max_length=30)
    propellants = models.ForeignKey(Fuel_Oxidizer_Mix, on_delete=models.PROTECT)
    mixture_ratio = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    cycle = models.CharField(max_length=30, blank=True)
    specific_impulse_vac = models.IntegerField() # stored in m/s
    specific_impulse_sl = models.IntegerField() # stored in m/s
    thrust_sl = models.IntegerField() # in newtons
    thrust_vac = models.IntegerField() # in newtons
    twr = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    chamber_pressure = models.IntegerField(blank=True) # stored in pascals
    rated_burn_time = models.SmallIntegerField(blank=True) # in seconds
    height = models.IntegerField(blank=True) # in milimeters
    diameter = models.IntegerField(blank=True) # in milimeters
    weight_dry = models.IntegerField(blank=True) # in grams
    gimbal_range = models.DecimalField(max_digits=4, decimal_places=1, blank=True)

class Stage(models.Model):


