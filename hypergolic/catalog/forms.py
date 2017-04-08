from django import forms
from .models import Role, StageRole, PowerCycle, Cooling, NozzleType,\
    NozzleMaterial, Injector, Igniter, Manufacturer, Compound, PropellantMix,\
    Engine, TankConstruction, TankMaterial, Stage, RocketSeries, Instrument,\
    GuidanceSystem, AntennaType, ElectricitySource, LifeSupportType,\
    AttitudeControlSystem, LandingSolution, HeatshieldMaterial, Organization,\
    MissionTarget, Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility,\
    Mission, Astronaut, CrewedMission


class BasicForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = ['name', 'description', 'illustration', 'sources']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        super(BasicForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(BasicForm, self).is_valid()

    def full_clean(self):
        return super(BasicForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(BasicForm, self).clean()

    def validate_unique(self):
        return super(BasicForm, self).validate_unique()

    def save(self, commit=True):
        return super(BasicForm, self).save(commit)


class RoleForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Role


class StageRoleForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = StageRole


class PowerCycleForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = PowerCycle


class CoolingForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Cooling


class NozzleTypeForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = NozzleType


class ChemForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = NozzleMaterial
        fields = ['name', 'chemical_formula', 'description', 'illustration',
                  'sources']


class NozzleMaterialForm(ChemForm):

    class Meta(ChemForm.Meta):
        model = NozzleMaterial


class InjectorForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Injector


class IgniterForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Igniter


class ManufacturerForm(BasicForm):

    class Meta:
        model = Manufacturer
        fields = ['name', 'native_name', 'country', 'headquarters',
                  'established', 'active', 'defunct', 'successor',
                  'description', 'website', 'illustration', 'sources']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        error_messages = {}

    def clean_established(self):
        established = self.cleaned_data.get("established", None)
        return established

    def clean_defunct(self):
        defunct = self.cleaned_data.get("defunct", None)
        return defunct

    def clean_successor(self):
        successor = self.cleaned_data.get("successor", None)
        return successor

    def clean_headquarters(self):
        headquarters = self.cleaned_data.get("headquarters", None)
        return headquarters

    def clean_website(self):
        website = self.cleaned_data.get("website", None)
        return website

    def clean(self):
        return super(ManufacturerForm, self).clean()

    def validate_unique(self):
        return super(ManufacturerForm, self).validate_unique()

    def save(self, commit=True):
        return super(ManufacturerForm, self).save(commit)


class CompoundForm(forms.ModelForm):

    class Meta:
        model = Compound
        fields = ['name', 'description', 'sources', 'role', 'chemical_formula', 'also_known_as', 'variety_of', 'density', 'melting_point', 'boiling_point', 'appearance', 'toxicity', 'storability', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CompoundForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CompoundForm, self).is_valid()

    def full_clean(self):
        return super(CompoundForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_role(self):
        role = self.cleaned_data.get("role", None)
        return role

    def clean_chemical_formula(self):
        chemical_formula = self.cleaned_data.get("chemical_formula", None)
        return chemical_formula

    def clean_also_known_as(self):
        also_known_as = self.cleaned_data.get("also_known_as", None)
        return also_known_as

    def clean_variety_of(self):
        variety_of = self.cleaned_data.get("variety_of", None)
        return variety_of

    def clean_density(self):
        density = self.cleaned_data.get("density", None)
        return density

    def clean_melting_point(self):
        melting_point = self.cleaned_data.get("melting_point", None)
        return melting_point

    def clean_boiling_point(self):
        boiling_point = self.cleaned_data.get("boiling_point", None)
        return boiling_point

    def clean_appearance(self):
        appearance = self.cleaned_data.get("appearance", None)
        return appearance

    def clean_toxicity(self):
        toxicity = self.cleaned_data.get("toxicity", None)
        return toxicity

    def clean_storability(self):
        storability = self.cleaned_data.get("storability", None)
        return storability

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(CompoundForm, self).clean()

    def validate_unique(self):
        return super(CompoundForm, self).validate_unique()

    def save(self, commit=True):
        return super(CompoundForm, self).save(commit)


class PropellantMixForm(forms.ModelForm):

    class Meta:
        model = PropellantMix
        fields = ['propellants', 'abbreviation', 'hypergolic', 'specific_impulse', 'specific_impulse_sl', 'characteristic_velocity', 'optimum_ratio', 'combustion_temp', 'description', 'sources']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PropellantMixForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PropellantMixForm, self).is_valid()

    def full_clean(self):
        return super(PropellantMixForm, self).full_clean()

    def clean_abbreviation(self):
        abbreviation = self.cleaned_data.get("abbreviation", None)
        return abbreviation

    def clean_hypergolic(self):
        hypergolic = self.cleaned_data.get("hypergolic", None)
        return hypergolic

    def clean_specific_impulse(self):
        specific_impulse = self.cleaned_data.get("specific_impulse", None)
        return specific_impulse

    def clean_specific_impulse_sl(self):
        specific_impulse_sl = self.cleaned_data.get("specific_impulse_sl", None)
        return specific_impulse_sl

    def clean_characteristic_velocity(self):
        characteristic_velocity = self.cleaned_data.get("characteristic_velocity", None)
        return characteristic_velocity

    def clean_optimum_ratio(self):
        optimum_ratio = self.cleaned_data.get("optimum_ratio", None)
        return optimum_ratio

    def clean_combustion_temp(self):
        combustion_temp = self.cleaned_data.get("combustion_temp", None)
        return combustion_temp

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean(self):
        return super(PropellantMixForm, self).clean()

    def validate_unique(self):
        return super(PropellantMixForm, self).validate_unique()

    def save(self, commit=True):
        return super(PropellantMixForm, self).save(commit)


class EngineForm(forms.ModelForm):

    class Meta:
        model = Engine
        fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'application', 'propellants', 'mixture_ratio', 'cycle', 'specific_impulse_vac', 'specific_impulse_sl', 'thrust_sl', 'thrust_vac', 'twr', 'chamber_pressure', 'combustion_chambers', 'rated_burn_time', 'nozzle_ratio', 'nozzle_shape', 'nozzle_material', 'cooling_method', 'injector_type', 'coefficient_of_thrust_vac', 'coefficient_of_thrust_sl', 'ignition_method', 'restart_capability', 'num_restarts', 'throttle_range_min', 'throttle_range_max', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(EngineForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(EngineForm, self).is_valid()

    def full_clean(self):
        return super(EngineForm, self).full_clean()

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_variant_of(self):
        variant_of = self.cleaned_data.get("variant_of", None)
        return variant_of

    def clean_native_name(self):
        native_name = self.cleaned_data.get("native_name", None)
        return native_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get("manufacturer", None)
        return manufacturer

    def clean_developed(self):
        developed = self.cleaned_data.get("developed", None)
        return developed

    def clean_first_flight(self):
        first_flight = self.cleaned_data.get("first_flight", None)
        return first_flight

    def clean_height(self):
        height = self.cleaned_data.get("height", None)
        return height

    def clean_diameter(self):
        diameter = self.cleaned_data.get("diameter", None)
        return diameter

    def clean_dry_weight(self):
        dry_weight = self.cleaned_data.get("dry_weight", None)
        return dry_weight

    def clean_application(self):
        application = self.cleaned_data.get("application", None)
        return application

    def clean_propellants(self):
        propellants = self.cleaned_data.get("propellants", None)
        return propellants

    def clean_mixture_ratio(self):
        mixture_ratio = self.cleaned_data.get("mixture_ratio", None)
        return mixture_ratio

    def clean_cycle(self):
        cycle = self.cleaned_data.get("cycle", None)
        return cycle

    def clean_specific_impulse_vac(self):
        specific_impulse_vac = self.cleaned_data.get("specific_impulse_vac", None)
        return specific_impulse_vac

    def clean_specific_impulse_sl(self):
        specific_impulse_sl = self.cleaned_data.get("specific_impulse_sl", None)
        return specific_impulse_sl

    def clean_thrust_sl(self):
        thrust_sl = self.cleaned_data.get("thrust_sl", None)
        return thrust_sl

    def clean_thrust_vac(self):
        thrust_vac = self.cleaned_data.get("thrust_vac", None)
        return thrust_vac

    def clean_twr(self):
        twr = self.cleaned_data.get("twr", None)
        return twr

    def clean_chamber_pressure(self):
        chamber_pressure = self.cleaned_data.get("chamber_pressure", None)
        return chamber_pressure

    def clean_combustion_chambers(self):
        combustion_chambers = self.cleaned_data.get("combustion_chambers", None)
        return combustion_chambers

    def clean_rated_burn_time(self):
        rated_burn_time = self.cleaned_data.get("rated_burn_time", None)
        return rated_burn_time

    def clean_nozzle_ratio(self):
        nozzle_ratio = self.cleaned_data.get("nozzle_ratio", None)
        return nozzle_ratio

    def clean_nozzle_shape(self):
        nozzle_shape = self.cleaned_data.get("nozzle_shape", None)
        return nozzle_shape

    def clean_nozzle_material(self):
        nozzle_material = self.cleaned_data.get("nozzle_material", None)
        return nozzle_material

    def clean_cooling_method(self):
        cooling_method = self.cleaned_data.get("cooling_method", None)
        return cooling_method

    def clean_injector_type(self):
        injector_type = self.cleaned_data.get("injector_type", None)
        return injector_type

    def clean_coefficient_of_thrust_vac(self):
        coefficient_of_thrust_vac = self.cleaned_data.get("coefficient_of_thrust_vac", None)
        return coefficient_of_thrust_vac

    def clean_coefficient_of_thrust_sl(self):
        coefficient_of_thrust_sl = self.cleaned_data.get("coefficient_of_thrust_sl", None)
        return coefficient_of_thrust_sl

    def clean_ignition_method(self):
        ignition_method = self.cleaned_data.get("ignition_method", None)
        return ignition_method

    def clean_restart_capability(self):
        restart_capability = self.cleaned_data.get("restart_capability", None)
        return restart_capability

    def clean_num_restarts(self):
        num_restarts = self.cleaned_data.get("num_restarts", None)
        return num_restarts

    def clean_throttle_range_min(self):
        throttle_range_min = self.cleaned_data.get("throttle_range_min", None)
        return throttle_range_min

    def clean_throttle_range_max(self):
        throttle_range_max = self.cleaned_data.get("throttle_range_max", None)
        return throttle_range_max

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(EngineForm, self).clean()

    def validate_unique(self):
        return super(EngineForm, self).validate_unique()

    def save(self, commit=True):
        return super(EngineForm, self).save(commit)


class TankConstructionForm(forms.ModelForm):

    class Meta:
        model = TankConstruction
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(TankConstructionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(TankConstructionForm, self).is_valid()

    def full_clean(self):
        return super(TankConstructionForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(TankConstructionForm, self).clean()

    def validate_unique(self):
        return super(TankConstructionForm, self).validate_unique()

    def save(self, commit=True):
        return super(TankConstructionForm, self).save(commit)


class TankMaterialForm(forms.ModelForm):

    class Meta:
        model = TankMaterial
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(TankMaterialForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(TankMaterialForm, self).is_valid()

    def full_clean(self):
        return super(TankMaterialForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(TankMaterialForm, self).clean()

    def validate_unique(self):
        return super(TankMaterialForm, self).validate_unique()

    def save(self, commit=True):
        return super(TankMaterialForm, self).save(commit)


class StageForm(forms.ModelForm):

    class Meta:
        model = Stage
        fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'stage_role', 'dry_weight', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'main_gimbal_yaw_min', 'main_gimbal_yaw_max', 'main_gimbal_pitch_min', 'main_gimbal_pitch_max', 'aux_engine', 'num_aux_engines', 'aux_gimbal_yaw_min', 'aux_gimbal_yaw_max', 'aux_gimbal_pitch_min', 'aux_gimbal_pitch_max', 'tank_type', 'tank_material', 'fins', 'burn_time', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StageForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StageForm, self).is_valid()

    def full_clean(self):
        return super(StageForm, self).full_clean()

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_variant_of(self):
        variant_of = self.cleaned_data.get("variant_of", None)
        return variant_of

    def clean_native_name(self):
        native_name = self.cleaned_data.get("native_name", None)
        return native_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get("manufacturer", None)
        return manufacturer

    def clean_developed(self):
        developed = self.cleaned_data.get("developed", None)
        return developed

    def clean_first_flight(self):
        first_flight = self.cleaned_data.get("first_flight", None)
        return first_flight

    def clean_height(self):
        height = self.cleaned_data.get("height", None)
        return height

    def clean_diameter(self):
        diameter = self.cleaned_data.get("diameter", None)
        return diameter

    def clean_stage_role(self):
        stage_role = self.cleaned_data.get("stage_role", None)
        return stage_role

    def clean_dry_weight(self):
        dry_weight = self.cleaned_data.get("dry_weight", None)
        return dry_weight

    def clean_fueled_weight(self):
        fueled_weight = self.cleaned_data.get("fueled_weight", None)
        return fueled_weight

    def clean_oxidizer_volume(self):
        oxidizer_volume = self.cleaned_data.get("oxidizer_volume", None)
        return oxidizer_volume

    def clean_fuel_volume(self):
        fuel_volume = self.cleaned_data.get("fuel_volume", None)
        return fuel_volume

    def clean_oxidizer_weight(self):
        oxidizer_weight = self.cleaned_data.get("oxidizer_weight", None)
        return oxidizer_weight

    def clean_fuel_weight(self):
        fuel_weight = self.cleaned_data.get("fuel_weight", None)
        return fuel_weight

    def clean_main_engine(self):
        main_engine = self.cleaned_data.get("main_engine", None)
        return main_engine

    def clean_num_main_engines(self):
        num_main_engines = self.cleaned_data.get("num_main_engines", None)
        return num_main_engines

    def clean_main_gimbal_yaw_min(self):
        main_gimbal_yaw_min = self.cleaned_data.get("main_gimbal_yaw_min", None)
        return main_gimbal_yaw_min

    def clean_main_gimbal_yaw_max(self):
        main_gimbal_yaw_max = self.cleaned_data.get("main_gimbal_yaw_max", None)
        return main_gimbal_yaw_max

    def clean_main_gimbal_pitch_min(self):
        main_gimbal_pitch_min = self.cleaned_data.get("main_gimbal_pitch_min", None)
        return main_gimbal_pitch_min

    def clean_main_gimbal_pitch_max(self):
        main_gimbal_pitch_max = self.cleaned_data.get("main_gimbal_pitch_max", None)
        return main_gimbal_pitch_max

    def clean_aux_engine(self):
        aux_engine = self.cleaned_data.get("aux_engine", None)
        return aux_engine

    def clean_num_aux_engines(self):
        num_aux_engines = self.cleaned_data.get("num_aux_engines", None)
        return num_aux_engines

    def clean_aux_gimbal_yaw_min(self):
        aux_gimbal_yaw_min = self.cleaned_data.get("aux_gimbal_yaw_min", None)
        return aux_gimbal_yaw_min

    def clean_aux_gimbal_yaw_max(self):
        aux_gimbal_yaw_max = self.cleaned_data.get("aux_gimbal_yaw_max", None)
        return aux_gimbal_yaw_max

    def clean_aux_gimbal_pitch_min(self):
        aux_gimbal_pitch_min = self.cleaned_data.get("aux_gimbal_pitch_min", None)
        return aux_gimbal_pitch_min

    def clean_aux_gimbal_pitch_max(self):
        aux_gimbal_pitch_max = self.cleaned_data.get("aux_gimbal_pitch_max", None)
        return aux_gimbal_pitch_max

    def clean_tank_type(self):
        tank_type = self.cleaned_data.get("tank_type", None)
        return tank_type

    def clean_tank_material(self):
        tank_material = self.cleaned_data.get("tank_material", None)
        return tank_material

    def clean_fins(self):
        fins = self.cleaned_data.get("fins", None)
        return fins

    def clean_burn_time(self):
        burn_time = self.cleaned_data.get("burn_time", None)
        return burn_time

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(StageForm, self).clean()

    def validate_unique(self):
        return super(StageForm, self).validate_unique()

    def save(self, commit=True):
        return super(StageForm, self).save(commit)


class RocketSeriesForm(forms.ModelForm):

    class Meta:
        model = RocketSeries
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RocketSeriesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RocketSeriesForm, self).is_valid()

    def full_clean(self):
        return super(RocketSeriesForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(RocketSeriesForm, self).clean()

    def validate_unique(self):
        return super(RocketSeriesForm, self).validate_unique()

    def save(self, commit=True):
        return super(RocketSeriesForm, self).save(commit)


class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(InstrumentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(InstrumentForm, self).is_valid()

    def full_clean(self):
        return super(InstrumentForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_energy_consumption(self):
        energy_consumption = self.cleaned_data.get("energy_consumption", None)
        return energy_consumption

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(InstrumentForm, self).clean()

    def validate_unique(self):
        return super(InstrumentForm, self).validate_unique()

    def save(self, commit=True):
        return super(InstrumentForm, self).save(commit)


class GuidanceSystemForm(forms.ModelForm):

    class Meta:
        model = GuidanceSystem
        fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(GuidanceSystemForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(GuidanceSystemForm, self).is_valid()

    def full_clean(self):
        return super(GuidanceSystemForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_energy_consumption(self):
        energy_consumption = self.cleaned_data.get("energy_consumption", None)
        return energy_consumption

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(GuidanceSystemForm, self).clean()

    def validate_unique(self):
        return super(GuidanceSystemForm, self).validate_unique()

    def save(self, commit=True):
        return super(GuidanceSystemForm, self).save(commit)


class AntennaTypeForm(forms.ModelForm):

    class Meta:
        model = AntennaType
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AntennaTypeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AntennaTypeForm, self).is_valid()

    def full_clean(self):
        return super(AntennaTypeForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(AntennaTypeForm, self).clean()

    def validate_unique(self):
        return super(AntennaTypeForm, self).validate_unique()

    def save(self, commit=True):
        return super(AntennaTypeForm, self).save(commit)


class ElectricitySourceForm(forms.ModelForm):

    class Meta:
        model = ElectricitySource
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ElectricitySourceForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ElectricitySourceForm, self).is_valid()

    def full_clean(self):
        return super(ElectricitySourceForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(ElectricitySourceForm, self).clean()

    def validate_unique(self):
        return super(ElectricitySourceForm, self).validate_unique()

    def save(self, commit=True):
        return super(ElectricitySourceForm, self).save(commit)


class LifeSupportTypeForm(forms.ModelForm):

    class Meta:
        model = LifeSupportType
        fields = ['name', 'description', 'sources', 'energy_consumption', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(LifeSupportTypeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(LifeSupportTypeForm, self).is_valid()

    def full_clean(self):
        return super(LifeSupportTypeForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_energy_consumption(self):
        energy_consumption = self.cleaned_data.get("energy_consumption", None)
        return energy_consumption

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(LifeSupportTypeForm, self).clean()

    def validate_unique(self):
        return super(LifeSupportTypeForm, self).validate_unique()

    def save(self, commit=True):
        return super(LifeSupportTypeForm, self).save(commit)


class AttitudeControlSystemForm(forms.ModelForm):

    class Meta:
        model = AttitudeControlSystem
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AttitudeControlSystemForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AttitudeControlSystemForm, self).is_valid()

    def full_clean(self):
        return super(AttitudeControlSystemForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(AttitudeControlSystemForm, self).clean()

    def validate_unique(self):
        return super(AttitudeControlSystemForm, self).validate_unique()

    def save(self, commit=True):
        return super(AttitudeControlSystemForm, self).save(commit)


class LandingSolutionForm(forms.ModelForm):

    class Meta:
        model = LandingSolution
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(LandingSolutionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(LandingSolutionForm, self).is_valid()

    def full_clean(self):
        return super(LandingSolutionForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(LandingSolutionForm, self).clean()

    def validate_unique(self):
        return super(LandingSolutionForm, self).validate_unique()

    def save(self, commit=True):
        return super(LandingSolutionForm, self).save(commit)


class HeatshieldMaterialForm(forms.ModelForm):

    class Meta:
        model = HeatshieldMaterial
        fields = ['name', 'description', 'sources', 'illustration', 'chemical_formula']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(HeatshieldMaterialForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(HeatshieldMaterialForm, self).is_valid()

    def full_clean(self):
        return super(HeatshieldMaterialForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean_chemical_formula(self):
        chemical_formula = self.cleaned_data.get("chemical_formula", None)
        return chemical_formula

    def clean(self):
        return super(HeatshieldMaterialForm, self).clean()

    def validate_unique(self):
        return super(HeatshieldMaterialForm, self).validate_unique()

    def save(self, commit=True):
        return super(HeatshieldMaterialForm, self).save(commit)


class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(OrganizationForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(OrganizationForm, self).is_valid()

    def full_clean(self):
        return super(OrganizationForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(OrganizationForm, self).clean()

    def validate_unique(self):
        return super(OrganizationForm, self).validate_unique()

    def save(self, commit=True):
        return super(OrganizationForm, self).save(commit)


class MissionTargetForm(forms.ModelForm):

    class Meta:
        model = MissionTarget
        fields = ['name', 'description', 'sources', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(MissionTargetForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(MissionTargetForm, self).is_valid()

    def full_clean(self):
        return super(MissionTargetForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(MissionTargetForm, self).clean()

    def validate_unique(self):
        return super(MissionTargetForm, self).validate_unique()

    def save(self, commit=True):
        return super(MissionTargetForm, self).save(commit)


class RocketForm(forms.ModelForm):

    class Meta:
        model = Rocket
        fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'series', 'dry_weight', 'fueled_weight', 'guidance_system', 'fairing_height', 'fairing_width', 'num_flights', 'failures', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RocketForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RocketForm, self).is_valid()

    def full_clean(self):
        return super(RocketForm, self).full_clean()

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_variant_of(self):
        variant_of = self.cleaned_data.get("variant_of", None)
        return variant_of

    def clean_native_name(self):
        native_name = self.cleaned_data.get("native_name", None)
        return native_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get("manufacturer", None)
        return manufacturer

    def clean_developed(self):
        developed = self.cleaned_data.get("developed", None)
        return developed

    def clean_first_flight(self):
        first_flight = self.cleaned_data.get("first_flight", None)
        return first_flight

    def clean_height(self):
        height = self.cleaned_data.get("height", None)
        return height

    def clean_diameter(self):
        diameter = self.cleaned_data.get("diameter", None)
        return diameter

    def clean_series(self):
        series = self.cleaned_data.get("series", None)
        return series

    def clean_dry_weight(self):
        dry_weight = self.cleaned_data.get("dry_weight", None)
        return dry_weight

    def clean_fueled_weight(self):
        fueled_weight = self.cleaned_data.get("fueled_weight", None)
        return fueled_weight

    def clean_guidance_system(self):
        guidance_system = self.cleaned_data.get("guidance_system", None)
        return guidance_system

    def clean_fairing_height(self):
        fairing_height = self.cleaned_data.get("fairing_height", None)
        return fairing_height

    def clean_fairing_width(self):
        fairing_width = self.cleaned_data.get("fairing_width", None)
        return fairing_width

    def clean_num_flights(self):
        num_flights = self.cleaned_data.get("num_flights", None)
        return num_flights

    def clean_failures(self):
        failures = self.cleaned_data.get("failures", None)
        return failures

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(RocketForm, self).clean()

    def validate_unique(self):
        return super(RocketForm, self).validate_unique()

    def save(self, commit=True):
        return super(RocketForm, self).save(commit)


class SpacecraftForm(forms.ModelForm):

    class Meta:
        model = Spacecraft
        fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system', 'battery_capacity', 'electricity_source', 'power_generation', 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield', 'landing_solution', 'num_flights', 'failures', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines', 'tank_type', 'tank_material', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SpacecraftForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SpacecraftForm, self).is_valid()

    def full_clean(self):
        return super(SpacecraftForm, self).full_clean()

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_variant_of(self):
        variant_of = self.cleaned_data.get("variant_of", None)
        return variant_of

    def clean_native_name(self):
        native_name = self.cleaned_data.get("native_name", None)
        return native_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get("manufacturer", None)
        return manufacturer

    def clean_developed(self):
        developed = self.cleaned_data.get("developed", None)
        return developed

    def clean_first_flight(self):
        first_flight = self.cleaned_data.get("first_flight", None)
        return first_flight

    def clean_height(self):
        height = self.cleaned_data.get("height", None)
        return height

    def clean_diameter(self):
        diameter = self.cleaned_data.get("diameter", None)
        return diameter

    def clean_dry_weight(self):
        dry_weight = self.cleaned_data.get("dry_weight", None)
        return dry_weight

    def clean_guidance_system(self):
        guidance_system = self.cleaned_data.get("guidance_system", None)
        return guidance_system

    def clean_attitude_control_system(self):
        attitude_control_system = self.cleaned_data.get("attitude_control_system", None)
        return attitude_control_system

    def clean_battery_capacity(self):
        battery_capacity = self.cleaned_data.get("battery_capacity", None)
        return battery_capacity

    def clean_electricity_source(self):
        electricity_source = self.cleaned_data.get("electricity_source", None)
        return electricity_source

    def clean_power_generation(self):
        power_generation = self.cleaned_data.get("power_generation", None)
        return power_generation

    def clean_antenna_type(self):
        antenna_type = self.cleaned_data.get("antenna_type", None)
        return antenna_type

    def clean_antenna_gain(self):
        antenna_gain = self.cleaned_data.get("antenna_gain", None)
        return antenna_gain

    def clean_transmitter_power(self):
        transmitter_power = self.cleaned_data.get("transmitter_power", None)
        return transmitter_power

    def clean_heatshield(self):
        heatshield = self.cleaned_data.get("heatshield", None)
        return heatshield

    def clean_landing_solution(self):
        landing_solution = self.cleaned_data.get("landing_solution", None)
        return landing_solution

    def clean_num_flights(self):
        num_flights = self.cleaned_data.get("num_flights", None)
        return num_flights

    def clean_failures(self):
        failures = self.cleaned_data.get("failures", None)
        return failures

    def clean_fueled_weight(self):
        fueled_weight = self.cleaned_data.get("fueled_weight", None)
        return fueled_weight

    def clean_oxidizer_volume(self):
        oxidizer_volume = self.cleaned_data.get("oxidizer_volume", None)
        return oxidizer_volume

    def clean_fuel_volume(self):
        fuel_volume = self.cleaned_data.get("fuel_volume", None)
        return fuel_volume

    def clean_oxidizer_weight(self):
        oxidizer_weight = self.cleaned_data.get("oxidizer_weight", None)
        return oxidizer_weight

    def clean_fuel_weight(self):
        fuel_weight = self.cleaned_data.get("fuel_weight", None)
        return fuel_weight

    def clean_main_engine(self):
        main_engine = self.cleaned_data.get("main_engine", None)
        return main_engine

    def clean_num_main_engines(self):
        num_main_engines = self.cleaned_data.get("num_main_engines", None)
        return num_main_engines

    def clean_aux_engine(self):
        aux_engine = self.cleaned_data.get("aux_engine", None)
        return aux_engine

    def clean_num_aux_engines(self):
        num_aux_engines = self.cleaned_data.get("num_aux_engines", None)
        return num_aux_engines

    def clean_tank_type(self):
        tank_type = self.cleaned_data.get("tank_type", None)
        return tank_type

    def clean_tank_material(self):
        tank_material = self.cleaned_data.get("tank_material", None)
        return tank_material

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(SpacecraftForm, self).clean()

    def validate_unique(self):
        return super(SpacecraftForm, self).validate_unique()

    def save(self, commit=True):
        return super(SpacecraftForm, self).save(commit)


class CrewedSpacecraftForm(forms.ModelForm):

    class Meta:
        model = CrewedSpacecraft
        fields = ['description', 'sources', 'name', 'country', 'variant_of', 'native_name', 'manufacturer', 'developed', 'first_flight', 'height', 'diameter', 'dry_weight', 'guidance_system', 'attitude_control_system', 'battery_capacity', 'electricity_source', 'power_generation', 'antenna_type', 'antenna_gain', 'transmitter_power', 'heatshield', 'landing_solution', 'num_flights', 'failures', 'fueled_weight', 'oxidizer_volume', 'fuel_volume', 'oxidizer_weight', 'fuel_weight', 'main_engine', 'num_main_engines', 'aux_engine', 'num_aux_engines', 'tank_type', 'tank_material', 'illustration', 'spacecraft_ptr', 'crew', 'life_support', 'supplies_days', 'pressurized_volume']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CrewedSpacecraftForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CrewedSpacecraftForm, self).is_valid()

    def full_clean(self):
        return super(CrewedSpacecraftForm, self).full_clean()

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_variant_of(self):
        variant_of = self.cleaned_data.get("variant_of", None)
        return variant_of

    def clean_native_name(self):
        native_name = self.cleaned_data.get("native_name", None)
        return native_name

    def clean_manufacturer(self):
        manufacturer = self.cleaned_data.get("manufacturer", None)
        return manufacturer

    def clean_developed(self):
        developed = self.cleaned_data.get("developed", None)
        return developed

    def clean_first_flight(self):
        first_flight = self.cleaned_data.get("first_flight", None)
        return first_flight

    def clean_height(self):
        height = self.cleaned_data.get("height", None)
        return height

    def clean_diameter(self):
        diameter = self.cleaned_data.get("diameter", None)
        return diameter

    def clean_dry_weight(self):
        dry_weight = self.cleaned_data.get("dry_weight", None)
        return dry_weight

    def clean_guidance_system(self):
        guidance_system = self.cleaned_data.get("guidance_system", None)
        return guidance_system

    def clean_attitude_control_system(self):
        attitude_control_system = self.cleaned_data.get("attitude_control_system", None)
        return attitude_control_system

    def clean_battery_capacity(self):
        battery_capacity = self.cleaned_data.get("battery_capacity", None)
        return battery_capacity

    def clean_electricity_source(self):
        electricity_source = self.cleaned_data.get("electricity_source", None)
        return electricity_source

    def clean_power_generation(self):
        power_generation = self.cleaned_data.get("power_generation", None)
        return power_generation

    def clean_antenna_type(self):
        antenna_type = self.cleaned_data.get("antenna_type", None)
        return antenna_type

    def clean_antenna_gain(self):
        antenna_gain = self.cleaned_data.get("antenna_gain", None)
        return antenna_gain

    def clean_transmitter_power(self):
        transmitter_power = self.cleaned_data.get("transmitter_power", None)
        return transmitter_power

    def clean_heatshield(self):
        heatshield = self.cleaned_data.get("heatshield", None)
        return heatshield

    def clean_landing_solution(self):
        landing_solution = self.cleaned_data.get("landing_solution", None)
        return landing_solution

    def clean_num_flights(self):
        num_flights = self.cleaned_data.get("num_flights", None)
        return num_flights

    def clean_failures(self):
        failures = self.cleaned_data.get("failures", None)
        return failures

    def clean_fueled_weight(self):
        fueled_weight = self.cleaned_data.get("fueled_weight", None)
        return fueled_weight

    def clean_oxidizer_volume(self):
        oxidizer_volume = self.cleaned_data.get("oxidizer_volume", None)
        return oxidizer_volume

    def clean_fuel_volume(self):
        fuel_volume = self.cleaned_data.get("fuel_volume", None)
        return fuel_volume

    def clean_oxidizer_weight(self):
        oxidizer_weight = self.cleaned_data.get("oxidizer_weight", None)
        return oxidizer_weight

    def clean_fuel_weight(self):
        fuel_weight = self.cleaned_data.get("fuel_weight", None)
        return fuel_weight

    def clean_main_engine(self):
        main_engine = self.cleaned_data.get("main_engine", None)
        return main_engine

    def clean_num_main_engines(self):
        num_main_engines = self.cleaned_data.get("num_main_engines", None)
        return num_main_engines

    def clean_aux_engine(self):
        aux_engine = self.cleaned_data.get("aux_engine", None)
        return aux_engine

    def clean_num_aux_engines(self):
        num_aux_engines = self.cleaned_data.get("num_aux_engines", None)
        return num_aux_engines

    def clean_tank_type(self):
        tank_type = self.cleaned_data.get("tank_type", None)
        return tank_type

    def clean_tank_material(self):
        tank_material = self.cleaned_data.get("tank_material", None)
        return tank_material

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean_spacecraft_ptr(self):
        spacecraft_ptr = self.cleaned_data.get("spacecraft_ptr", None)
        return spacecraft_ptr

    def clean_crew(self):
        crew = self.cleaned_data.get("crew", None)
        return crew

    def clean_life_support(self):
        life_support = self.cleaned_data.get("life_support", None)
        return life_support

    def clean_supplies_days(self):
        supplies_days = self.cleaned_data.get("supplies_days", None)
        return supplies_days

    def clean_pressurized_volume(self):
        pressurized_volume = self.cleaned_data.get("pressurized_volume", None)
        return pressurized_volume

    def clean(self):
        return super(CrewedSpacecraftForm, self).clean()

    def validate_unique(self):
        return super(CrewedSpacecraftForm, self).validate_unique()

    def save(self, commit=True):
        return super(CrewedSpacecraftForm, self).save(commit)


class LaunchFacilityForm(forms.ModelForm):

    class Meta:
        model = LaunchFacility
        fields = ['name', 'description', 'sources', 'location', 'owning_country', 'latitude', 'longitude', 'elevation', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(LaunchFacilityForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(LaunchFacilityForm, self).is_valid()

    def full_clean(self):
        return super(LaunchFacilityForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_location(self):
        location = self.cleaned_data.get("location", None)
        return location

    def clean_owning_country(self):
        owning_country = self.cleaned_data.get("owning_country", None)
        return owning_country

    def clean_latitude(self):
        latitude = self.cleaned_data.get("latitude", None)
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get("longitude", None)
        return longitude

    def clean_elevation(self):
        elevation = self.cleaned_data.get("elevation", None)
        return elevation

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(LaunchFacilityForm, self).clean()

    def validate_unique(self):
        return super(LaunchFacilityForm, self).validate_unique()

    def save(self, commit=True):
        return super(LaunchFacilityForm, self).save(commit)


class MissionForm(forms.ModelForm):

    class Meta:
        model = Mission
        fields = ['name', 'description', 'sources', 'country', 'organization', 'launch_date', 'end_date', 'launch_facility', 'launch_vehicle', 'spacecraft', 'failure', 'illustration']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(MissionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(MissionForm, self).is_valid()

    def full_clean(self):
        return super(MissionForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_organization(self):
        organization = self.cleaned_data.get("organization", None)
        return organization

    def clean_launch_date(self):
        launch_date = self.cleaned_data.get("launch_date", None)
        return launch_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get("end_date", None)
        return end_date

    def clean_launch_facility(self):
        launch_facility = self.cleaned_data.get("launch_facility", None)
        return launch_facility

    def clean_launch_vehicle(self):
        launch_vehicle = self.cleaned_data.get("launch_vehicle", None)
        return launch_vehicle

    def clean_spacecraft(self):
        spacecraft = self.cleaned_data.get("spacecraft", None)
        return spacecraft

    def clean_failure(self):
        failure = self.cleaned_data.get("failure", None)
        return failure

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean(self):
        return super(MissionForm, self).clean()

    def validate_unique(self):
        return super(MissionForm, self).validate_unique()

    def save(self, commit=True):
        return super(MissionForm, self).save(commit)


class AstronautForm(forms.ModelForm):

    class Meta:
        model = Astronaut
        fields = ['first_name', 'middle_names', 'last_name', 'nationality', 'organization', 'birth_date', 'birth_place', 'death_date', 'biography', 'sources', 'picture']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AstronautForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AstronautForm, self).is_valid()

    def full_clean(self):
        return super(AstronautForm, self).full_clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", None)
        return first_name

    def clean_middle_names(self):
        middle_names = self.cleaned_data.get("middle_names", None)
        return middle_names

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", None)
        return last_name

    def clean_nationality(self):
        nationality = self.cleaned_data.get("nationality", None)
        return nationality

    def clean_organization(self):
        organization = self.cleaned_data.get("organization", None)
        return organization

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date", None)
        return birth_date

    def clean_birth_place(self):
        birth_place = self.cleaned_data.get("birth_place", None)
        return birth_place

    def clean_death_date(self):
        death_date = self.cleaned_data.get("death_date", None)
        return death_date

    def clean_biography(self):
        biography = self.cleaned_data.get("biography", None)
        return biography

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_picture(self):
        picture = self.cleaned_data.get("picture", None)
        return picture

    def clean(self):
        return super(AstronautForm, self).clean()

    def validate_unique(self):
        return super(AstronautForm, self).validate_unique()

    def save(self, commit=True):
        return super(AstronautForm, self).save(commit)


class CrewedMissionForm(forms.ModelForm):

    class Meta:
        model = CrewedMission
        fields = ['name', 'description', 'sources', 'country', 'organization', 'launch_date', 'end_date', 'launch_facility', 'launch_vehicle', 'spacecraft', 'failure', 'illustration', 'landing_site']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CrewedMissionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CrewedMissionForm, self).is_valid()

    def full_clean(self):
        return super(CrewedMissionForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_sources(self):
        sources = self.cleaned_data.get("sources", None)
        return sources

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_organization(self):
        organization = self.cleaned_data.get("organization", None)
        return organization

    def clean_launch_date(self):
        launch_date = self.cleaned_data.get("launch_date", None)
        return launch_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get("end_date", None)
        return end_date

    def clean_launch_facility(self):
        launch_facility = self.cleaned_data.get("launch_facility", None)
        return launch_facility

    def clean_launch_vehicle(self):
        launch_vehicle = self.cleaned_data.get("launch_vehicle", None)
        return launch_vehicle

    def clean_spacecraft(self):
        spacecraft = self.cleaned_data.get("spacecraft", None)
        return spacecraft

    def clean_failure(self):
        failure = self.cleaned_data.get("failure", None)
        return failure

    def clean_illustration(self):
        illustration = self.cleaned_data.get("illustration", None)
        return illustration

    def clean_mission_ptr(self):
        mission_ptr = self.cleaned_data.get("mission_ptr", None)
        return mission_ptr

    def clean_landing_site(self):
        landing_site = self.cleaned_data.get("landing_site", None)
        return landing_site

    def clean(self):
        return super(CrewedMissionForm, self).clean()

    def validate_unique(self):
        return super(CrewedMissionForm, self).validate_unique()

    def save(self, commit=True):
        return super(CrewedMissionForm, self).save(commit)

