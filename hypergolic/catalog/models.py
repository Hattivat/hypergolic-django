from django.db import models

# Create your models here.
YEARS = (x for x in range(1950, 2030))

class Role(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True)

class PowerCycle(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    native_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    established = models.SmallIntegerField(choices=YEARS, blank=True)
    active = models.BooleanField(blank=True)
    defunct = models.SmallIntegerField(choices=YEARS, blank=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    image = models.ImageField(blank=True)

class Compound(models.Model):
    name = models.CharField(max_lenght=100, primary_key=True, unique=True)
    role = models.BooleanField() # true = fuel, false = oxidizer
    chem_formula = models.CharField(max_length=30)
    density = models.FloatField()
    melting_point = models.DecimalField(max_digits=6, decimal_places=2) # in degrees Celsius
    boiling_point = models.DecimalField(max_digits=6, decimal_places=2) # in degrees Celsius
    appearance = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(max_length=20, blank=True)
    storability = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

class FuelOxidizerMix(models.Model):
    fuel = models.ForeignKey(Compound, on_delete=models.CASCADE, limit_choices_to={'role': True})
    oxidizer = models.ForeignKey(Compound, on_delete=models.CASCADE, limit_choices_to={'role': False})
    hypergolic = models.BooleanField()
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
    developed = models.SmallIntegerField(choices=YEARS, blank=True)
    first_flight = models.SmallIntegerField(choices=YEARS, blank=True)
    application = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True)
    propellants = models.ForeignKey(FuelOxidizerMix, on_delete=models.PROTECT)
    mixture_ratio = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    cycle = models.ForeignKey(PowerCycle, on_delete=models.SET_NULL, blank=True)
    specific_impulse_vac = models.IntegerField() # stored in m/s
    specific_impulse_sl = models.IntegerField() # stored in m/s
    thrust_sl = models.IntegerField() # stored in newtons
    thrust_vac = models.IntegerField() # stored in newtons
    twr = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    chamber_pressure = models.IntegerField(blank=True) # stored in pascals
    rated_burn_time = models.SmallIntegerField(blank=True) # in seconds
    nozzle_ratio = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    height = models.IntegerField(blank=True) # stored in milimeters
    diameter = models.IntegerField(blank=True) # stored in milimeters
    weight_dry = models.IntegerField(blank=True) # stored in grams
    gimbal_range = models.DecimalField(max_digits=4, decimal_places=1, blank=True)
    coefficient_of_thrust_vac = models.FloatField(blank=True)
    coefficient_of_thrust_sl = models.FloatField(blank=True)
    ignition_method = models.CharField(blank=True)
    restart_capability = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

class Stage(models.Model):
    name = models.CharField(max_length=50)
    developed = models.DateField
    empty_mass = models.IntegerField() # stored in grams
    fueled_mass = models.integerField() # stored in grams
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT)
    num_main_engines = models.SmallIntegerField()
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT, blank=True)
    num_aux_engines = models.SmallIntegerField(blank=True)
    height = models.IntegerField() # stored in milimiters
    diameter = models.IntegerField() # stored in milimiters
    burn_time = models.IntegerField(blank=True) # in seconds
    image = models.ImageField(blank=True)
