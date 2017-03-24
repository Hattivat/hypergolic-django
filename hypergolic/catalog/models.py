from django.db import models
from .constants import YEARS, DEGREES, COUNTRIES


class Basic(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Role(Basic):
    illustration = models.ImageField(blank=True, upload_to='engineroles/')


class StageRole(Basic):
    illustration = models.ImageField(blank=True, upload_to='stageroles/')


class PowerCycle(Basic):
    illustration = models.ImageField(blank=True, upload_to='powercycles/')


class Cooling(Basic):
    illustration = models.ImageField(blank=True, upload_to='coolingmethods/')


class NozzleType(Basic):
    illustration = models.ImageField(blank=True, upload_to='nozzletypes/')


class NozzleMaterial(Basic):
    chemical_formula = models.CharField(max_leght=30, blank=True)
    illustration = models.ImageField(blank=True, upload_to='nozzlematerials/')


class Injector(Basic):
    illustration = models.ImageField(blank=True, upload_to='injectors/')


class Manufacturer(Basic):
    native_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    established = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    active = models.BooleanField(blank=True)
    defunct = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    illustration = models.ImageField(blank=True, upload_to='manufacturers/')


class Compound(Basic):
    role = models.BooleanField()  # true = fuel, false = oxidizer
    chem_formula = models.CharField(max_length=30)
    density = models.FloatField()
    # melting_point and boiling_point in degrees Celsius
    melting_point = models.DecimalField(max_digits=6, decimal_places=2)
    boiling_point = models.DecimalField(max_digits=6, decimal_places=2)
    appearance = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(max_length=20, choices=DEGREES, blank=True)
    storability = models.CharField(max_length=20, choices=DEGREES, blank=True)
    illustration = models.ImageField(blank=True, upload_to='chemcompounds/')


class FuelOxidizerMix(models.Model):
    fuel = models.ForeignKey(Compound, on_delete=models.CASCADE,
                             limit_choices_to={'role': True})
    oxidizer = models.ForeignKey(Compound, on_delete=models.CASCADE, null=True,
                                 limit_choices_to={'role': False}, blank=True)
    hypergolic = models.BooleanField()
    specific_impulse = models.PositiveIntegerField()  # stored in m/s
    specific_impulse_sl = models.PositiveIntegerField(blank=True)  # in m/s
    optimum_ratio = models.DecimalField(max_digits=5, decimal_places=2,
                                        blank=True)
    combustion_temp = models.DecimalField(max_digits=6, decimal_places=1,
                                          blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Complex(Basic):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    variant_of = models.ForeignKey('self', on_delete=models.SET_NULL,
                                   blank=True, null=True)
    native_name = models.CharField(max_length=50, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT,
                                     blank=True, null=True)
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    height = models.PositiveIntegerField(blank=True)  # stored in milimeters
    diameter = models.PositiveIntegerField(blank=True)  # stored in milimeters
    dry_weight = models.PositiveIntegerField(blank=True)  # stored in grams

    class Meta:
        abstract = True


class Engine(Complex):
    application = models.ForeignKey(Role, on_delete=models.SET_NULL,
                                    blank=True, null=True)
    propellants = models.ForeignKey(FuelOxidizerMix, on_delete=models.PROTECT)
    mixture_ratio = models.DecimalField(max_digits=8, decimal_places=4,
                                        blank=True)
    cycle = models.ForeignKey(PowerCycle, on_delete=models.SET_NULL,
                              blank=True, null=True)
    specific_impulse_vac = models.PositiveIntegerField()  # stored in m/s
    specific_impulse_sl = models.PositiveIntegerField()  # stored in m/s
    thrust_sl = models.PositiveIntegerField()  # stored in newtons
    thrust_vac = models.PositiveIntegerField()  # stored in newtons
    twr = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    chamber_pressure = models.PositiveIntegerField(blank=True)  # pascals
    rated_burn_time = models.PositiveSmallIntegerField(blank=True)  # seconds
    nozzle_ratio = models.DecimalField(max_digits=6, decimal_places=2,
                                       blank=True)
    nozzle_shape = models.ForeignKey(NozzleType, on_delete=models.PROTECT,
                                     blank=True, null=True)
    nozzle_material = models.ForeignKey(NozzleMaterial,
                                        on_delete=models.PROTECT,
                                        blank=True, null=True)
    cooling_method = models.ForeignKey(Cooling, on_delete=models.PROTECT,
                                       blank=True, null=True)
    injector_type = models.ForeignKey(Injector, on_delete=models.PROTECT,
                                      blank=True, null=True)
    gimbal_range = models.DecimalField(max_digits=4, decimal_places=1,
                                       blank=True)
    coefficient_of_thrust_vac = models.FloatField(blank=True)
    coefficient_of_thrust_sl = models.FloatField(blank=True)
    ignition_method = models.CharField(blank=True)
    restart_capability = models.BooleanField(default=False)
    num_restarts = models.PositiveSmallIntegerField(default=0, blank=True)
    throttle_range_min = models.PositiveSmallIntegerField(default=100,
                                                          blank=True)
    throttle_range_max = models.PositiveSmallIntegerField(default=100,
                                                          blank=True)
    illustration = models.ImageField(blank=True, upload_to='engines/')


class TankConstruction(Basic):
    illustration = models.ImageField(blank=True, upload_to='tanktypes/')


class TankMaterial(Basic):
    illustration = models.ImageField(blank=True, upload_to='tankmaterials/')


class Stage(Complex):
    fueled_weight = models.PositiveIntegerField()  # stored in grams
    oxidizer_volume = models.PositiveIntegerField(blank=True)  # in litres
    fuel_volume = models.PositiveIntegerField(blank=True)  # in litres
    oxidizer_weight = models.PositiveIntegerField(blank=True)  # in kilograms
    fuel_weight = models.PositiveIntegerField(blank=True)  # in kilograms
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT)
    num_main_engines = models.PositiveSmallIntegerField(default=1)
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                   blank=True)
    num_aux_engines = models.PositiveSmallIntegerField(blank=True, default=0)
    tank_type = models.ForeignKey(TankConstruction, on_delete=models.SET_NULL,
                                  blank=True, null=True)
    tank_material = models.ForeignKey(TankMaterial, on_delete=models.SET_NULL,
                                      blank=True, null=True)
    fins = models.PositiveSmallIntegerField(default=0)
    burn_time = models.PositiveIntegerField(blank=True)  # in seconds
    illustration = models.ImageField(blank=True, upload_to='stages/')


class RocketSeries(Basic):
    illustration = models.ImageField(blank=True, upload_to='rocketseries/')


class Instrument(Basic):
    energy_consumption = models.PositiveIntegerField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='instruments/')


class GuidanceSystem(Basic):
    energy_consumption = models.PositiveIntegerField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='guidancesystems/')


class AntennaType(Basic):
    illustration = models.ImageField(blank=True, upload_to='antennatypes/')


class ElectricitySource(Basic):
    illustration = models.ImageField(blank=True, upload_to='electrsources/')


class LifeSupportType(Basic):
    energy_consumption = models.PositiveIntegerField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='lifesupport/')


class AttitudeControlSystem(Basic):
    illustration = models.ImageField(blank=True, upload_to='attitudesystems/')


class LandingSolution(Basic):
    illustration = models.ImageField(blank=True, upload_to='landingsolutions/')


class HeatshieldMaterial(Basic):
    illustration = models.ImageField(blank=True,
                                     upload_to='heatshieldmaterials/')
    chem_formula = models.CharField(max_length=30, blank=True)


class Organization(Basic):
    illustration = models.ImageField(blank=True, upload_to='organizations/')


class Rocket(Complex):
    series = models.ForeignKey(RocketSeries, on_delete=models.PROTECT,
                               blank=True)
    stages = models.ManyToManyField(Stage)
    fueled_weight = models.PositiveIntegerField()  # stored in grams
    guidance_system = models.ForeignKey(GuidanceSystem, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    num_flights = models.PositiveSmallIntegerField(default=0)
    failures = models.PositiveSmallIntegerField(default=0)
    illustration = models.ImageField(blank=True, upload_to='rockets/')


class Spacecraft(Stage):
    instruments = models.ManyToManyField(Instrument, blank=True, null=True,
                                         on_delete=models.SET_NULL)
    guidance_system = models.ForeignKey(GuidanceSystem, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    attitude_control_system = models.ForeignKey(AttitudeControlSystem,
                                                on_delete=models.SET_NULL,
                                                blank=True, null=True)
    battery_capacity = models.PositiveIntegerField(blank=True)  # in watthours
    electricity_source = models.ForeignKey(ElectricitySource, blank=True,
                                           on_delete=models.SET_NULL,
                                           null=True)
    power_generation = models.PositiveIntegerField(blank=True)  # in watts
    antenna_type = models.ForeignKey(AntennaType, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    antenna_gain = models.PositiveSmallIntegerField(blank=True)  # in dBi
    transmitter_power = models.PositiveIntegerField(blank=True)  # in watts
    heatshield = models.ForeignKey(HeatshieldMaterial, blank=True, null=True,
                                   on_delete=models.PROTECT)
    landing_solution = models.ForeignKey(LandingSolution, blank=True,
                                         null=True, on_delete=models.PROTECT)
    num_flights = models.PositiveSmallIntegerField(default=0)
    failures = models.PositiveSmallIntegerField(default=0)
    illustration = models.ImageField(blank=True, upload_to='spacecrafts/')


class CrewedSpacecraft(Spacecraft):
    crew = models.PositiveSmallIntegerField(default=1)
    life_support = models.ForeignKey(LifeSupportType, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    supplies_days = models.PositiveSmallIntegerField(blank=True)
    pressurized_volume = models.PositiveSmallIntegerField(blank=True)  # in m3


class LaunchFacility(Basic):
    location = models.CharField(max_length=50)
    owning_country = models.CharField(max_length=50, choices=COUNTRIES)
    latitude = models.PositiveSmallIntegerField()
    longitude = models.PositiveSmallIntegerField()
    elevation = models.PositiveSmallIntegerField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='launchfacilities/')


class Mission(Basic):
    country = models.CharField(max_length=50, choices=COUNTRIES)
    organization = models.ForeignField(Organization, on_delete=models.PROTECT,
                                       blank=True)
    launch_date = models.DateTimeField()
    end_date = models.DateTimeField()
    launch_facility = models.ForeignKey(LaunchFacility,
                                        on_delete=models.PROTECT)
    launch_vehicle = models.ForeignKey(Rocket, on_delete=models.PROTECT)
    spacecraft = models.ForeignKey(Spacecraft, on_delete=models.PROTECT)
    target = models.CharField(max_length=200)
    failure = models.BooleanField(default=False)
    illustration = models.ImageField(blank=True, upload_to='missions/')


class Astronaut(models.Model):
    first_name = models.CharField(max_length=50)
    middle_names = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, choices=COUNTRIES)
    organization = models.ForeignField(Organization, on_delete=models.PROTECT,
                                       blank=True)
    birth_date = models.DateTimeField(blank=True)
    birth_place = models.CharField(max_length=100)
    death_date = models.DateTimeField(blank=True)
    biography = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='astronauts/')

    def __str__(self):
        return self.first_name + self.middle_names + self.last_name


class CrewedMission(Mission):
    crew = models.ManyToManyField(Astronaut, on_delete=models.PROTECT)
    landing_site = models.CharField(max_length=100, blank=True)
