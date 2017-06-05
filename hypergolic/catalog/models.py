from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .constants import YEARS, DEGREES, COUNTRIES
from .helpers import underscore


class Basic(models.Model):
    """An abstract model serving as a generic base for most other models in
    this app."""

    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True, help_text="Please use your own \
                                   words and do not plagiarise content from \
                                   elsewhere.")
    sources = models.TextField(help_text="Please list the sources you have \
                               used to obtain/verify the information you are \
                               adding.")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('{}_detail'.format(underscore(self.__class__.__name__)),
                       kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('{}_create'.format(underscore(self.__class__.__name__)))

    def get_update_url(self):
        return reverse('{}_update'.format(underscore(self.__class__.__name__)),
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('{}_delete'.format(underscore(self.__class__.__name__)),
                       kwargs={'pk': self.pk})

    def get_list_url(self):
        return reverse('{}_list'.format(underscore(self.__class__.__name__)))

    class Meta:
        abstract = True
        ordering = ['name']


class Role(Basic):
    """A model for engine roles, e.g. 'first stage', 'vernier', 'landing'."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='engine_roles_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='engine_roles_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='engineroles/')

    class Meta:
        verbose_name = "Engine role"
        verbose_name_plural = "Engine roles"


class StageRole(Basic):
    """A model for stage roles, e.g. 'first stage', 'third stage', 'lunar
    ascent stage'."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='stage_roles_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='stage_roles_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='stageroles/')


class PowerCycle(Basic):
    """A model for storing rocket engine power cycles, such as 'gas generator'
    or 'expander cycle'."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='power_cycles_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='power_cycles_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='powercycles/')


class Cooling(Basic):
    """A model for cooling solutions, such as 'ablative', 'regenerative
    (corrugated metal shell)', etc."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='cooling_methods_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='coolig_methods_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='coolingmethods/')

    class Meta:
        verbose_name = "Cooling system"
        verbose_name_plural = "Cooling systems"


class NozzleType(Basic):
    """A model for nozzle types, generally shapes."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='nozzle_types_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='nozzle_types_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='nozzletypes/')


class NozzleMaterial(Basic):
    """A model for materials used to construct rocket nozzles."""

    chemical_formula = models.CharField(max_length=30, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='nozzle_materials_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='nozzle_materials_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='nozzlematerials/')


class Injector(Basic):
    """A model for types of rocket engine injectors."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='injectors_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='injectors_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='injectors/')


class Igniter(Basic):
    """A model for rocket engine ignition solutions."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='igniters_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='igniters_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='igniters/')


class Manufacturer(Basic):
    """A model for manufacturers of space equipment."""

    native_name = models.CharField(max_length=100, blank=True, help_text="The \
                                   name of the manufacturer as it would appear\
                                   in its native language and script.")
    country = models.CharField(max_length=50, choices=COUNTRIES)
    established = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                                   null=True)
    active = models.NullBooleanField(blank=True, null=True, help_text="Is \
                                     the company still alive and producing \
                                     things under its logo, as opposed to \
                                     being defunct or merged into some other \
                                     company?")
    defunct = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                               null=True, help_text="If the \
                                               company is no longer active, \
                                               please give the year it ceased \
                                               operating.")
    successor = models.ForeignKey('self', blank=True, null=True,
                                  related_name="predecessor", help_text="If \
                                  the company was merged with/into some other \
                                  organization, please tell us its name.")
    headquarters = models.CharField(max_length=100, blank=True, help_text="The \
                                    city and country in which this \
                                    manufacturer's headquarters are located.")
    website = models.URLField(max_length=100, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='manufacturers_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='manufacturers_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='manufacturers/')


class Compound(Basic):
    """A model for chemical compounds used for propulsion."""

    role = models.BooleanField(choices=((True, 'Fuel'), (False, 'Oxidizer')),
                               help_text="Is this compound used as a fuel, \
                               or as an oxidizer? In case of a monopropellant,\
                               choose the fuel setting.")
    chemical_formula = models.CharField(max_length=30, blank=True)
    also_known_as = models.CharField(max_length=50, blank=True)
    variety_of = models.ForeignKey('self', on_delete=models.SET_NULL,
                                   blank=True, null=True,
                                   related_name="version")
    density = models.DecimalField(max_digits=6, decimal_places=4, blank=True,
                                  null=True, help_text="In g/ml")
    melting_point = models.DecimalField(max_digits=6, decimal_places=2,
                                        blank=True, null=True, help_text="In \
                                        Kelvins")
    boiling_point = models.DecimalField(max_digits=6, decimal_places=2,
                                        blank=True, null=True, help_text="In \
                                        Kelvins")
    appearance = models.CharField(max_length=250, blank=True, help_text="Use \
                                  adjectives, such as 'transparent', or \
                                  'reddish brown'.")
    toxicity = models.CharField(max_length=20, choices=DEGREES, blank=True,
                                help_text="How dangerous the compound and/or \
                                the compounds created in its combustion are \
                                for humans in case of skin contact or \
                                inhalation (disregard oral ingestion, as it \
                                is unlikely to happen involuntarily).")
    storability = models.CharField(max_length=20, choices=DEGREES, blank=True,
                                   help_text="How quickly the compound boils \
                                   off or otherwise spoils in typical \
                                   conditions. For example, Liquid Hydrogen \
                                   scores 'very low', while a typical solid \
                                   rocket fuel scores 'very high'.")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='compounds_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='compounds_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='chemcompounds/')


class PropellantMix(models.Model):
    """A model for propellant mixtures used for propulsion. This usually
    means a fuel/oxidizer pair, but we also allow for more exotic
    solutions."""

    propellants = models.ManyToManyField(Compound, help_text="The chemical \
                                         compounds used in this mixture, \
                                         typically although not exclusivily \
                                         one oxidizer and one fuel compound.")
    abbreviation = models.CharField(max_length=30, blank=True, help_text="A \
                                    shorter way to refer to the propellant \
                                    combination, often colloquial (e.g. \
                                    'hydrolox').")
    hypergolic = models.BooleanField(default=False, help_text="Whether or not \
                                     this particular combination of chemical \
                                     compounds ignites spontaneusly (without \
                                     an external spark or flame) on contact. \
                                     If unsure, leave it at 'False'.")
    specific_impulse = models.DecimalField(max_digits=10, decimal_places=1,
                                           help_text="In seconds",
                                           verbose_name="Theoretical specific \
                                           impulse in vacuum")
    characteristic_velocity = models.PositiveIntegerField(blank=True,
                                                          null=True,
                                                          help_text="In m/s")
    optimum_ratio = models.DecimalField(max_digits=5, decimal_places=2,
                                        blank=True, null=True, help_text="As \
                                        a ratio of 'x to 1'.")
    combustion_temp = models.DecimalField(max_digits=6, decimal_places=1,
                                          blank=True, null=True,
                                          verbose_name="combustion \
                                          temperature", help_text="In Kelvins")
    description = models.TextField(blank=True, help_text="Please use your own \
                                   words and do not plagiarise content from \
                                   elsewhere.")
    sources = models.TextField(help_text="Please list the sources you have \
                               used to obtain/verify the information you are \
                               adding.")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='propellant_mixes_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='propellant_mixes_modified')

    def __str__(self):
        mix = (propellant.name for propellant in self.propellants.all())
        return "/".join(mix)

    def get_absolute_url(self):
        return reverse('propellant_mix_detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_create_url():
        return reverse('propellant_mix_create')

    def get_update_url(self):
        return reverse('propellant_mix_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('propellant_mix_delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_list_url():
        return reverse('propellant_mix_list')

    class Meta:
        verbose_name_plural = "Propellant mixes"


class Complex(Basic):
    """An abstract model to serve as a base for models of the most complex
    pieces of spacefaring equipment, such as engines, spacecraft, etc."""

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    variant_of = models.ForeignKey('self', on_delete=models.SET_NULL,
                                   blank=True, null=True)
    native_name = models.CharField(max_length=50, blank=True, help_text="The\
                                   name of the part as it would appear in the \
                                   native language and script of its \
                                   manufacturer.")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT,
                                     blank=True, null=True)
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                                 null=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True,
                                                    null=True)
    height = models.DecimalField(max_digits=8, decimal_places=4, blank=True,
                                 null=True, help_text="In metres.")
    diameter = models.DecimalField(max_digits=8, decimal_places=4, blank=True,
                                   null=True, help_text="In metres.")
    dry_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                   blank=True, null=True,
                                   help_text="In kilograms.")

    class Meta:
        abstract = True


class Engine(Complex):
    """A model for all sorts of rocket engines."""

    application = models.ForeignKey(Role, on_delete=models.SET_NULL,
                                    blank=True, null=True, help_text="The \
                                    role in which this engine is usually \
                                    employed.")
    propellants = models.ForeignKey(PropellantMix, on_delete=models.PROTECT)
    mixture_ratio = models.DecimalField(max_digits=8, decimal_places=4,
                                        blank=True, null=True,
                                        help_text="The ratio of oxidizer \
                                        to fuel used in this engine.")
    cycle = models.ForeignKey(PowerCycle, on_delete=models.SET_NULL,
                              blank=True, null=True, help_text="The power \
                              cycle employed in this engine, e.g. 'staged \
                              combustion'.")
    specific_impulse_vac = models.DecimalField(max_digits=10, decimal_places=1,
                                               help_text="In seconds",
                                               verbose_name="Specific \
                                               impulse in vacuum.")
    specific_impulse_sl = models.DecimalField(max_digits=10, decimal_places=1,
                                              help_text="In seconds",
                                              verbose_name="Specific \
                                              impulse at sea level.")
    thrust_sl = models.DecimalField(max_digits=10, decimal_places=4,
                                    help_text="In kilonewtons")
    thrust_vac = models.DecimalField(max_digits=10, decimal_places=4,
                                     help_text="In kilonewtons")
    twr = models.DecimalField(max_digits=6, decimal_places=2, blank=True,
                              verbose_name="Thrust-to-mass Ratio")
    chamber_pressure = models.DecimalField(max_digits=10, decimal_places=4,
                                           blank=True, null=True,
                                           help_text="In kilopascals")
    combustion_chambers = models.PositiveSmallIntegerField(default=1,
                                                           help_text="The \
                                                           number of \
                                                           combustion chambers\
                                                            this engine has, \
                                                           almost always one.")
    rated_burn_time = models.PositiveSmallIntegerField(blank=True, null=True,
                                                       help_text="In seconds")
    nozzle_ratio = models.DecimalField(max_digits=6, decimal_places=2,
                                       blank=True, null=True, help_text="The \
                                       ratio of the area of nozzle exit to \
                                       the area of nozzle throat. Also known \
                                       as section ratio or expansion ratio.")
    nozzle_shape = models.ForeignKey(NozzleType, on_delete=models.PROTECT,
                                     blank=True, null=True)
    nozzle_material = models.ForeignKey(NozzleMaterial,
                                        on_delete=models.PROTECT,
                                        blank=True, null=True)
    cooling_method = models.ForeignKey(Cooling, on_delete=models.PROTECT,
                                       blank=True, null=True)
    injector_type = models.ForeignKey(Injector, on_delete=models.PROTECT,
                                      blank=True, null=True)
    coefficient_of_thrust_vac = models.FloatField(blank=True, null=True,
                                                  verbose_name="Coefficient \
                                                  of thrust in vacuum")
    coefficient_of_thrust_sl = models.FloatField(blank=True, null=True,
                                                 verbose_name="Coefficient of \
                                                 thrust at sea level")
    ignition_method = models.ForeignKey(Igniter, on_delete=models.SET_NULL,
                                        blank=True, null=True)
    restart_capability = models.BooleanField(default=False, help_text="Whether\
                                              or not the engine can be \
                                              restarted in flight. For the \
                                              overwhelming majority of rocket \
                                              engines the answer is 'no'.")
    num_restarts = models.PositiveSmallIntegerField(default=0, blank=True,
                                                    null=True, verbose_name="\
                                                    number of restarts",
                                                    help_text="How many times \
                                                    the rocket can be safely \
                                                    restarted in flight.")
    throttle_range_min = models.PositiveSmallIntegerField(default=100,
                                                          blank=True,
                                                          null=True,
                                                          help_text="As a \
                                                          percentage of rated \
                                                          thrust")
    throttle_range_max = models.PositiveSmallIntegerField(default=100,
                                                          blank=True,
                                                          null=True,
                                                          help_text="As a \
                                                          percentage of rated \
                                                          thrust; confusingly,\
                                                           can be over 100.")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='engines_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='engines_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='engines/')


class TankConstruction(Basic):
    """A model for rocket propellant tank construction types."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='tank_constructions_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='tank_constructions_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='tanktypes/')


class TankMaterial(Basic):
    """A model for materials used to construct rocket propellant tanks."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='tank_materials_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='tank_materials_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='tankmaterials/')


class Stage(Complex):
    """A model for all kinds of rocket stages."""

    stage_role = models.ForeignKey(StageRole, on_delete=models.PROTECT,
                                   null=True)
    fueled_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                      help_text="In kilograms.")
    oxidizer_volume = models.PositiveIntegerField(blank=True, null=True,
                                                  help_text="In litres")
    fuel_volume = models.PositiveIntegerField(blank=True, null=True,
                                              help_text="In litres")
    oxidizer_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                        blank=True, null=True,
                                        help_text="In kilograms.")
    fuel_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                    blank=True, null=True,
                                    help_text="In kilograms.")
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                    related_name='stage_main')
    num_main_engines = models.PositiveSmallIntegerField(default=1,
                                                        verbose_name="number \
                                                        of main engines")
    main_gimbal_yaw_min = models.DecimalField(max_digits=4, decimal_places=1,
                                              blank=True, null=True)
    main_gimbal_yaw_max = models.DecimalField(max_digits=4, decimal_places=1,
                                              blank=True, null=True)
    main_gimbal_pitch_min = models.DecimalField(max_digits=4, decimal_places=1,
                                                blank=True, null=True)
    main_gimbal_pitch_max = models.DecimalField(max_digits=4, decimal_places=1,
                                                blank=True, null=True)
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                   blank=True, null=True,
                                   related_name='stage_aux',
                                   verbose_name="auxilliary engine")
    num_aux_engines = models.PositiveSmallIntegerField(default=0,
                                                       verbose_name="number \
                                                       of auxilliary engines")
    aux_gimbal_yaw_min = models.DecimalField(max_digits=4, decimal_places=1,
                                             blank=True, null=True)
    aux_gimbal_yaw_max = models.DecimalField(max_digits=4, decimal_places=1,
                                             blank=True, null=True)
    aux_gimbal_pitch_min = models.DecimalField(max_digits=4, decimal_places=1,
                                               blank=True, null=True)
    aux_gimbal_pitch_max = models.DecimalField(max_digits=4, decimal_places=1,
                                               blank=True, null=True)
    aux_oxidizer_volume = models.PositiveIntegerField(blank=True, null=True,
                                                      help_text="In litres")
    aux_fuel_volume = models.PositiveIntegerField(blank=True, null=True,
                                                  help_text="In litres")
    aux_oxidizer_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                            blank=True, null=True,
                                            help_text="In kilograms.")
    aux_fuel_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                        blank=True, null=True,
                                        help_text="In kilograms.")
    tank_type = models.ForeignKey(TankConstruction, on_delete=models.SET_NULL,
                                  blank=True, null=True)
    tank_material = models.ForeignKey(TankMaterial, on_delete=models.SET_NULL,
                                      blank=True, null=True)
    pressurant = models.ForeignKey(Compound, on_delete=models.SET_NULL,
                                   blank=True, null=True)
    fins = models.PositiveSmallIntegerField(default=0)
    burn_time = models.PositiveIntegerField(blank=True, null=True,
                                            help_text="In seconds")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='stages_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='stages_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='stages/')


class RocketSeries(Basic):
    """A model to store rocket families, such as 'Atlas' or 'Ariane'."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='rocket_series_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='rocket_series_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='rocketseries/')

    class Meta:
        verbose_name_plural = "Rocket series"


class Instrument(Basic):
    """A model for all kinds of scientific instruments used in space."""

    energy_consumption = models.PositiveIntegerField(blank=True, null=True,
                                                     help_text="In watts")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='instruments_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='instruments_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='instruments/')


class GuidanceSystem(Basic):
    """A model for types of guidance systems used in rocketry."""

    energy_consumption = models.PositiveIntegerField(blank=True, null=True,
                                                     help_text="In watts")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='guidance_systems_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='guidance_systems_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='guidancesystems/')


class AntennaType(Basic):
    """A model for types of antennas used on spacecraft."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='antenna_types_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='antenna_types_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='antennatypes/')


class ElectricitySource(Basic):
    """A model for kinds of electricity sources used in space, such as
    solar panels or RTG generators."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='electricity_sources_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='electricity_sources_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='electrsources/')


class LifeSupportType(Basic):
    """A model for types of life support systems used in spacecraft, focusing
    mostly on the chemical compounds used."""

    energy_consumption = models.PositiveIntegerField(blank=True, null=True,
                                                     help_text="In watts")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='lss_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='lss_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='lifesupport/')


class AttitudeControlSystem(Basic):
    """A model for kinds of attitude control systems employed by spacecraft.
    This typically means RCS engines, but there are other options."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='acs_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='acs_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='attitudesystems/')


class LandingSolution(Basic):
    """A model for landing solutions, such as 'propulsive', 'parachutes',
    'glider', etc."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='landing_solutions_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='landing_solutions_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='landingsolutions/')


class HeatshieldMaterial(Basic):
    """A model for materials used to construct heatshields for spacecraft."""

    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='heatshieldmaterials/')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='heatshield_materials_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='heatshield_materials_modified')
    chemical_formula = models.CharField(max_length=30, blank=True, null=True)


class Organization(Basic):
    """A model for spacefaring organizations, such as NASA, or ESA. This is
    intended first and foremost to reflect multi-national efforts and allow
    us to distinguish between different organizations within a country, e.g.
    NASA vs. USAF missions."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='organizations_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='organizations_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='organizations/')


class MissionTarget(Basic):
    """A model for mission targets, generally meaning astronomical objects,
    e.g. 'Mars', 'Halley's comet', 'Titan'."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='mission_targets_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='mission_targets_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='missiontargets/')


class Rocket(Complex):
    """A model for rockets as whole units, without payload."""

    series = models.ForeignKey(RocketSeries, on_delete=models.PROTECT,
                               blank=True, null=True, help_text="If this \
                               rocket is part of a series, such as 'Ariane', \
                               or 'Saturn', you can specify it here.")
    stages = models.ManyToManyField(Stage)
    fueled_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                      blank=True, null=True,
                                      help_text="In kilograms.")
    guidance_system = models.ForeignKey(GuidanceSystem, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    battery_capacity = models.PositiveIntegerField(blank=True, null=True,
                                                   help_text="in watt-hours")
    fairing_height = models.DecimalField(max_digits=8, decimal_places=4,
                                         blank=True, null=True,
                                         help_text="in metres")
    fairing_width = models.DecimalField(max_digits=8, decimal_places=4,
                                        blank=True, null=True,
                                        help_text="in metres")
    fairing_mass = models.DecimalField(max_digits=11, decimal_places=3,
                                       blank=True, null=True, help_text="\
                                       in kilograms")
    payload_to_leo = models.DecimalField(max_digits=12, decimal_places=3,
                                         blank=True, null=True, help_text="\
                                         in kilograms")
    payload_to_gto = models.DecimalField(max_digits=12, decimal_places=3,
                                         blank=True, null=True, help_text="\
                                         in kilograms")
    payload_to_tli = models.DecimalField(max_digits=12, decimal_places=3,
                                         blank=True, null=True, help_text="\
                                         in kilograms")
    num_flights = models.PositiveSmallIntegerField(default=0,
                                                   verbose_name="number of \
                                                   flights")
    failures = models.PositiveSmallIntegerField(default=0, help_text="The \
                                                number of times this Rocket\
                                                has catastrophically failed\
                                                during a mission.")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='rockets_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='rockets_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='rockets/')

    def num_stages(self):
        return self.stages.count()


class Spacecraft(Complex):
    """A model for robotic (uncrewed) spacecraft of all kinds."""

    instruments = models.ManyToManyField(Instrument, blank=True, help_text="\
                                         scientific instruments present on \
                                         this spacecraft")
    guidance_system = models.ForeignKey(GuidanceSystem, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    attitude_control_system = models.ForeignKey(AttitudeControlSystem,
                                                on_delete=models.SET_NULL,
                                                blank=True, null=True)
    battery_capacity = models.PositiveIntegerField(blank=True, null=True,
                                                   help_text="in watt-hours")
    electricity_source = models.ForeignKey(ElectricitySource, blank=True,
                                           on_delete=models.SET_NULL,
                                           null=True)
    power_generation = models.PositiveIntegerField(blank=True, null=True,
                                                   help_text="in watts")
    antenna_type = models.ForeignKey(AntennaType, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    antenna_gain = models.PositiveSmallIntegerField(blank=True, null=True,
                                                    help_text="in dBi")
    transmitter_power = models.PositiveIntegerField(blank=True, null=True,
                                                    help_text="in watts")
    heatshield = models.ForeignKey(HeatshieldMaterial, blank=True, null=True,
                                   on_delete=models.PROTECT, help_text="If \
                                   this spacecraft is equipped with a \
                                   heatshield, please specify its type")
    landing_solution = models.ForeignKey(LandingSolution, blank=True,
                                         null=True, on_delete=models.PROTECT,
                                         help_text="If this spacecraft is \
                                         capable of landing, please specify \
                                         the means by which it achieves this \
                                         feat")
    num_flights = models.PositiveSmallIntegerField(default=0,
                                                   verbose_name='number of \
                                                   flights')
    failures = models.PositiveSmallIntegerField(default=0, help_text="The \
                                                number of times this \
                                                spacecraft (not the rocket \
                                                lifting it) has failed on a \
                                                mission")
    fueled_mass = models.DecimalField(max_digits=12, decimal_places=4,
                                      help_text="In kilograms.")
    oxidizer_volume = models.PositiveIntegerField(blank=True, null=True,
                                                  help_text="in litres")
    fuel_volume = models.PositiveIntegerField(blank=True, null=True,
                                              help_text="in litres")
    oxidizer_mass = models.DecimalField(max_digits=12, decimal_places=3,
                                        blank=True, null=True, help_text="\
                                        in kilograms")
    fuel_mass = models.DecimalField(max_digits=12, decimal_places=3,
                                    blank=True, null=True, help_text="\
                                    in kilograms")
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                    related_name='spacecraft_main')
    num_main_engines = models.PositiveSmallIntegerField(default=1,
                                                        verbose_name='number \
                                                        of main engines')
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT,
                                   blank=True, null=True,
                                   related_name='spacecraft_aux',
                                   verbose_name='auxilliary engine')
    num_aux_engines = models.PositiveSmallIntegerField(blank=True, default=0,
                                                       verbose_name='number \
                                                       of auxilliary engines')
    aux_oxidizer_volume = models.PositiveIntegerField(blank=True, null=True,
                                                      help_text="In litres")
    aux_fuel_volume = models.PositiveIntegerField(blank=True, null=True,
                                                  help_text="In litres")
    aux_oxidizer_mass = models.DecimalField(max_digits=12, decimal_places=3,
                                            blank=True, null=True, help_text="\
                                            in kilograms")
    aux_fuel_mass = models.DecimalField(max_digits=12, decimal_places=3,
                                        blank=True, null=True, help_text="\
                                        in kilograms")
    tank_type = models.ForeignKey(TankConstruction, on_delete=models.SET_NULL,
                                  blank=True, null=True)
    tank_material = models.ForeignKey(TankMaterial, on_delete=models.SET_NULL,
                                      blank=True, null=True)
    pressurant = models.ForeignKey(Compound, on_delete=models.SET_NULL,
                                   blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='spacecraft_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='spacecraft_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='spacecrafts/')


class CrewedSpacecraft(Spacecraft):
    """A model for all sorts of crewed (manned) spacecraft."""

    crew = models.PositiveSmallIntegerField(default=1)
    life_support = models.ForeignKey(LifeSupportType, blank=True, null=True,
                                     on_delete=models.SET_NULL)
    supplies_days = models.PositiveSmallIntegerField(blank=True, null=True,
                                                     help_text="For how many \
                                                     days could the life \
                                                     support supplies last.")
    pressurized_volume = models.DecimalField(max_digits=8, decimal_places=2,
                                             blank=True, null=True,
                                             help_text="pressurized (safe for \
                                             crew) space in cubic metres")


class LaunchFacility(Basic):
    """A model for launch facilities, such as the Baikonur cosmodrome."""

    location = models.CharField(max_length=50)
    owning_country = models.CharField(max_length=50, choices=COUNTRIES)
    latitude = models.PositiveSmallIntegerField()
    longitude = models.PositiveSmallIntegerField()
    elevation = models.PositiveSmallIntegerField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='launch_facilities_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='launch_facilities_modified')
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='launchfacilities/')

    class Meta:
        verbose_name_plural = "Launch facilities"


class BaseMission(Basic):
    """An abstract model serving as a base for CrewedMission and (robotic)
    Mission models"""

    country = models.CharField(max_length=50, choices=COUNTRIES)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT,
                                     blank=True, null=True)
    launch_date = models.DateTimeField()
    end_date = models.DateTimeField()
    launch_facility = models.ForeignKey(LaunchFacility,
                                        on_delete=models.PROTECT)
    launch_vehicle = models.ForeignKey(Rocket, on_delete=models.PROTECT,
                                       help_text="the rocket type used in \
                                       the mission")
    targets = models.ManyToManyField(MissionTarget, help_text="the places the \
                                     mission was supposed to reach")
    failure = models.BooleanField(default=False, help_text="whether or not \
                                  the mission ended in failure for whatever \
                                  reason")
    illustration = models.ImageField(blank=True, null=True,
                                     upload_to='missions/')

    def print_targets(self):
        return ', '.join([target.name for target in self.targets.all()])

    class Meta:
        abstract = True


class Mission(BaseMission):
    """A model for all sorts of uncrewed missions, test launches, etc."""

    spacecraft = models.ForeignKey(Spacecraft, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='missions_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='missions_modified')


class Astronaut(models.Model):
    """A model for astronauts/cosmonauts."""

    first_name = models.CharField(max_length=50)
    middle_names = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, choices=COUNTRIES)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT,
                                     blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    birth_place = models.CharField(max_length=100)
    death_date = models.DateTimeField(blank=True, null=True)
    biography = models.TextField(blank=True, help_text="Please use your own \
                                   words and do not plagiarise content from \
                                   elsewhere.")
    sources = models.TextField(help_text="Please list the sources you have \
                               used to obtain/verify the information you are \
                               adding.")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='astronauts_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='astronauts_modified')
    picture = models.ImageField(blank=True, null=True,
                                upload_to='astronauts/')

    def __str__(self):
        return self.first_name + self.middle_names + self.last_name

    def get_absolute_url(self):
        return reverse('astronaut_detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_create_url():
        return reverse('astronaut_create')

    def get_update_url(self):
        return reverse('astronaut_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('astronaut_delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_list_url():
        return reverse('astronaut_list')

    class Meta:
        ordering = ['last_name']


class CrewedMission(BaseMission):
    """A model for all kinds of manned missions/launches."""

    crew = models.ManyToManyField(Astronaut, help_text="the astronauts on \
                                  board the spacecraft")
    spacecraft = models.ForeignKey(CrewedSpacecraft, on_delete=models.PROTECT)
    landing_site = models.CharField(max_length=100, blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                related_name='crewed_missions_created')
    modifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 related_name='crewed_missions_modified')

    def print_crew(self):
        return ', '.join([target.__str__() for target in self.crew.all()])
