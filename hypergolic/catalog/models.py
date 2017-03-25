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
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='engineroles/')


class StageRole(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='stageroles/')


class PowerCycle(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='powercycles/')


class Cooling(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='coolingmethods/')


class NozzleType(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='nozzletypes/')


class NozzleMaterial(Basic):
    chemical_formula = models.CharField(max_length=30, blank=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='nozzlematerials/')


class Injector(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='injectors/')


class Igniter(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='igniters/')


class Manufacturer(Basic):
    native_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    established = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                                   null=True)
    active = models.NullBooleanField(blank=True, null=True)
    defunct = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                               null=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='manufacturers/')


class Compound(Basic):
    role = models.BooleanField(choices=((True, 'Fuel'), (False, 'Oxidizer')))
    chem_formula = models.CharField(max_length=30, blank=True)
    abbreviation = models.CharField(max_length=10, blank=True)
    variety_of = models.ForeignKey('self', on_delete=models.SET_NULL,
                                   blank=True, null=True,
                                   related_name="version")
    density = models.FloatField(blank=True, null=True)
    # melting_point and boiling_point in degrees Celsius
    melting_point = models.DecimalField(max_digits=6, decimal_places=2,
                                        blank=True, null=True)
    boiling_point = models.DecimalField(max_digits=6, decimal_places=2,
                                        blank=True, null=True)
    appearance = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(max_length=20, choices=DEGREES, blank=True)
    storability = models.CharField(max_length=20, choices=DEGREES, blank=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='chemcompounds/')


class FuelOxidizerMix(models.Model):
    fuel = models.ForeignKey(Compound, on_delete=models.CASCADE,
                             limit_choices_to={'role': True},
                             related_name='as_fuel')
    oxidizer = models.ForeignKey(Compound, on_delete=models.CASCADE, null=True,
                                 limit_choices_to={'role': False}, blank=True,
                                 related_name='as_oxidizer')
    hypergolic = models.BooleanField(default=False)
    specific_impulse = models.PositiveIntegerField()  # stored in m/s
    specific_impulse_sl = models.PositiveIntegerField(blank=True, null=True)
    optimum_ratio = models.DecimalField(max_digits=5, decimal_places=2,
                                        blank=True, null=True)
    combustion_temp = models.DecimalField(max_digits=6, decimal_places=1,
                                          blank=True, null=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

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
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                                 null=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                                    null=True)
    height = models.PositiveIntegerField(blank=True, null=True)  # stored in mm
    diameter = models.PositiveIntegerField(blank=True, null=True)  # milimeters
    dry_weight = models.PositiveIntegerField(blank=True, null=True)  # in grams

    class Meta:
        abstract = True


class Engine(Complex):
    application = models.ForeignKey(Role, on_delete=models.SET_NULL,
                                    blank=True, null=True)
    propellants = models.ForeignKey(FuelOxidizerMix, on_delete=models.PROTECT)
    mixture_ratio = models.DecimalField(max_digits=8, decimal_places=4,
                                        blank=True, null=True)
    cycle = models.ForeignKey(PowerCycle, on_delete=models.SET_NULL,
                              blank=True, null=True)
    specific_impulse_vac = models.PositiveIntegerField()  # stored in m/s
    specific_impulse_sl = models.PositiveIntegerField()  # stored in m/s
    thrust_sl = models.PositiveIntegerField()  # stored in newtons
    thrust_vac = models.PositiveIntegerField()  # stored in newtons
    twr = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    # chamber pressure is stored in Pascals
    chamber_pressure = models.PositiveIntegerField(blank=True, null=True)
    # rated burn time is stored in seconds
    rated_burn_time = models.PositiveSmallIntegerField(blank=True, null=True)
    nozzle_ratio = models.DecimalField(max_digits=6, decimal_places=2,
                                       blank=True, null=True)
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
                                       blank=True, null=True)
    coefficient_of_thrust_vac = models.FloatField(blank=True, null=True)
    coefficient_of_thrust_sl = models.FloatField(blank=True, null=True)
    ignition_method = models.ForeignKey(Igniter, on_delete=models.SET_NULL,
                                        blank=True, null=True)
    restart_capability = models.BooleanField(default=False)
    num_restarts = models.PositiveSmallIntegerField(default=0, blank=True,
                                                    null=True)
    throttle_range_min = models.PositiveSmallIntegerField(default=100,
                                                          blank=True,
                                                          null=True)
    throttle_range_max = models.PositiveSmallIntegerField(default=100,
                                                          blank=True,
                                                          null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='engines/')


class TankConstruction(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='tanktypes/')


class TankMaterial(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='tankmaterials/')


class Stage(Complex):
    fueled_weight = models.PositiveIntegerField()  # stored in grams
    # volumes are stored in litres
    oxidizer_volume = models.PositiveIntegerField(blank=True, null=True)
    fuel_volume = models.PositiveIntegerField(blank=True, null=True)
    # weights are stored in kilograms
    oxidizer_weight = models.PositiveIntegerField(blank=True, null=True)
    fuel_weight = models.PositiveIntegerField(blank=True, null=True)
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                    related_name='stage_main')
    num_main_engines = models.PositiveSmallIntegerField(default=1)
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                   blank=True, null=True,
                                   related_name='stage_aux')
    num_aux_engines = models.PositiveSmallIntegerField(default=0)
    tank_type = models.ForeignKey(TankConstruction, on_delete=models.SET_NULL,
                                  blank=True, null=True)
    tank_material = models.ForeignKey(TankMaterial, on_delete=models.SET_NULL,
                                      blank=True, null=True)
    fins = models.PositiveSmallIntegerField(default=0)
    burn_time = models.PositiveIntegerField(blank=True, null=True)  # seconds
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='stages/')


class RocketSeries(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='rocketseries/')


class Instrument(Basic):
    # energy consumption in watts
    energy_consumption = models.PositiveIntegerField(blank=True, null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='instruments/')


class GuidanceSystem(Basic):
    # energy consumption in watts
    energy_consumption = models.PositiveIntegerField(blank=True, null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='guidancesystems/')


class AntennaType(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='antennatypes/')


class ElectricitySource(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='electrsources/')


class LifeSupportType(Basic):
    # energy consumption in watts
    energy_consumption = models.PositiveIntegerField(blank=True, null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='lifesupport/')


class AttitudeControlSystem(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='attitudesystems/')


class LandingSolution(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='landingsolutions/')


class HeatshieldMaterial(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='heatshieldmaterials/')
    chem_formula = models.CharField(max_length=30, blank=True, null=True)


class Organization(Basic):
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='organizations/')


class Rocket(Complex):
    series = models.ForeignKey(RocketSeries, on_delete=models.PROTECT,
                               blank=True, null=True)
    stages = models.ManyToManyField(Stage)
    fueled_weight = models.PositiveIntegerField()  # stored in grams
    guidance_system = models.ForeignKey(GuidanceSystem, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    num_flights = models.PositiveSmallIntegerField(default=0)
    failures = models.PositiveSmallIntegerField(default=0)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='rockets/')


class Spacecraft(Complex):
    instruments = models.ManyToManyField(Instrument, blank=True)
    guidance_system = models.ForeignKey(GuidanceSystem, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    attitude_control_system = models.ForeignKey(AttitudeControlSystem,
                                                on_delete=models.SET_NULL,
                                                blank=True, null=True)
    # battery capacity in watthours, power generation in watts
    battery_capacity = models.PositiveIntegerField(blank=True, null=True)
    electricity_source = models.ForeignKey(ElectricitySource, blank=True,
                                           on_delete=models.SET_NULL,
                                           null=True)
    power_generation = models.PositiveIntegerField(blank=True, null=True)
    antenna_type = models.ForeignKey(AntennaType, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    # antenna gain in dBi, transmitter power in watts
    antenna_gain = models.PositiveSmallIntegerField(blank=True, null=True)
    transmitter_power = models.PositiveIntegerField(blank=True, null=True)
    heatshield = models.ForeignKey(HeatshieldMaterial, blank=True, null=True,
                                   on_delete=models.PROTECT)
    landing_solution = models.ForeignKey(LandingSolution, blank=True,
                                         null=True, on_delete=models.PROTECT)
    num_flights = models.PositiveSmallIntegerField(default=0)
    failures = models.PositiveSmallIntegerField(default=0)
    fueled_weight = models.PositiveIntegerField()  # stored in grams
    # volumes in litres, weights in grams
    oxidizer_volume = models.PositiveIntegerField(blank=True, null=True)
    fuel_volume = models.PositiveIntegerField(blank=True, null=True)
    oxidizer_weight = models.PositiveIntegerField(blank=True, null=True)
    fuel_weight = models.PositiveIntegerField(blank=True, null=True)
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                    related_name='spacecraft_main')
    num_main_engines = models.PositiveSmallIntegerField(default=1)
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                   blank=True, null=True,
                                   related_name='spacecraft_aux')
    num_aux_engines = models.PositiveSmallIntegerField(blank=True, default=0)
    tank_type = models.ForeignKey(TankConstruction, on_delete=models.SET_NULL,
                                  blank=True, null=True)
    tank_material = models.ForeignKey(TankMaterial, on_delete=models.SET_NULL,
                                      blank=True, null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='spacecrafts/')


class CrewedSpacecraft(Spacecraft):
    crew = models.PositiveSmallIntegerField(default=1)
    life_support = models.ForeignKey(LifeSupportType, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    supplies_days = models.PositiveSmallIntegerField(blank=True, null=True)
    # volume in litres
    pressurized_volume = models.PositiveIntegerField(blank=True, null=True)


class LaunchFacility(Basic):
    location = models.CharField(max_length=50)
    owning_country = models.CharField(max_length=50, choices=COUNTRIES)
    latitude = models.PositiveSmallIntegerField()
    longitude = models.PositiveSmallIntegerField()
    elevation = models.PositiveSmallIntegerField(blank=True, null=True)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='launchfacilities/')


class Mission(Basic):
    country = models.CharField(max_length=50, choices=COUNTRIES)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT,
                                     blank=True, null=True)
    launch_date = models.DateTimeField()
    end_date = models.DateTimeField()
    launch_facility = models.ForeignKey(LaunchFacility,
                                        on_delete=models.PROTECT)
    launch_vehicle = models.ForeignKey(Rocket, on_delete=models.PROTECT)
    spacecraft = models.ForeignKey(Spacecraft, on_delete=models.PROTECT)
    target = models.CharField(max_length=200)
    failure = models.BooleanField(default=False)
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='missions/')


class Astronaut(models.Model):
    first_name = models.CharField(max_length=50)
    middle_names = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, choices=COUNTRIES)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT,
                                     blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    birth_place = models.CharField(max_length=100)
    death_date = models.DateTimeField(blank=True, null=True)
    biography = models.TextField(blank=True)
    picture = models.ImageField(blank=True, null=True,
                                upload_to='astronauts/')

    def __str__(self):
        return self.first_name + self.middle_names + self.last_name


class CrewedMission(Mission):
    crew = models.ManyToManyField(Astronaut)
    landing_site = models.CharField(max_length=100, blank=True)
