from django import forms
from .models import Role, StageRole, PowerCycle, Cooling, NozzleType,\
    NozzleMaterial, Injector, Igniter, Manufacturer, Compound, PropellantMix,\
    Engine, TankConstruction, TankMaterial, Stage, RocketSeries, Instrument,\
    GuidanceSystem, AntennaType, ElectricitySource, LifeSupportType,\
    AttitudeControlSystem, LandingSolution, HeatshieldMaterial, Organization,\
    MissionTarget, Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility,\
    Mission, Astronaut, CrewedMission
from .helpers import wrong_year_order


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

    class Meta(BasicForm.Meta):
        model = Manufacturer
        fields = ['name', 'native_name', 'country', 'headquarters',
                  'established', 'active', 'defunct', 'successor',
                  'website', 'description', 'illustration', 'sources']

    def clean(self):
        cleaned_data = super(ManufacturerForm, self).clean()
        estab = cleaned_data.get('established')
        defun = cleaned_data.get('defunct')
        activ = cleaned_data.get('active')
        sucsr = cleaned_data.get('successor')
        if wrong_year_order(estab, defun):
            raise forms.ValidationError("A manufacturer cannot become \
                                        defunct before it is established")
        if activ is not False:
            if sucsr or defun:
                raise forms.ValidationError("Please set the 'active' field\
                                            to 'No' first.")
        return cleaned_data


class CompoundForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Compound
        fields = ['name', 'also_known_as', 'role', 'chemical_formula',
                  'variety_of', 'density', 'melting_point',
                  'boiling_point', 'appearance', 'toxicity', 'storability',
                  'description', 'illustration', 'sources']


class PropellantMixForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = PropellantMix
        fields = ['propellants', 'abbreviation', 'hypergolic',
                  'specific_impulse', 'specific_impulse_sl',
                  'characteristic_velocity', 'optimum_ratio',
                  'combustion_temp', 'description', 'sources']


class EngineForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Engine
        fields = ['name', 'native_name', 'application', 'country',
                  'manufacturer', 'variant_of', 'specific_impulse_vac',
                  'specific_impulse_sl', 'thrust_vac', 'thrust_sl', 'twr',
                  'coefficient_of_thrust_vac', 'coefficient_of_thrust_sl',
                  'rated_burn_time', 'height', 'diameter', 'dry_weight',
                  'cycle', 'injector_type', 'ignition_method', 'propellants',
                  'mixture_ratio', 'chamber_pressure', 'combustion_chambers',
                  'nozzle_ratio', 'nozzle_shape', 'nozzle_material',
                  'cooling_method', 'restart_capability', 'num_restarts',
                  'throttle_range_min', 'throttle_range_max', 'developed',
                  'first_flight', 'illustration', 'description', 'sources']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def clean(self):
        cleaned_data = super(EngineForm, self).clean()
        devel = cleaned_data.get('developed')
        flight = cleaned_data.get('first_flight')
        thr_min = cleaned_data.get('throttle_range_min')
        thr_max = cleaned_data.get('throttle_range_max')
        restarts = cleaned_data.get('number_of_restarts')
        restcap = cleaned_data.get('restart_capability')
        if wrong_year_order(devel, flight):
            raise forms.ValidationError("Things cannot fly before they are \
                                        developed")
        if thr_min > thr_max:
            raise forms.ValidationError("Minimum throttle cannot be greater \
                                        than maximum throttle")
        if not restcap and restarts > 0:
            raise forms.ValidationError("Please click on the 'restart \
                                        capability' checkbox first")
        return cleaned_data


class TankConstructionForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = TankConstruction


class TankMaterialForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = TankMaterial


class StageForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Stage
        fields = ['name', 'native_name', 'variant_of', 'stage_role', 'country',
                  'manufacturer', 'height', 'diameter',  'dry_weight',
                  'fueled_weight', 'tank_type', 'tank_material', 'fuel_volume',
                  'oxidizer_volume', 'fuel_weight', 'oxidizer_weight',
                  'main_engine', 'num_main_engines', 'aux_engine',
                  'num_aux_engines', 'burn_time', 'main_gimbal_yaw_min',
                  'main_gimbal_yaw_max', 'main_gimbal_pitch_min',
                  'main_gimbal_pitch_max', 'aux_gimbal_yaw_min',
                  'aux_gimbal_yaw_max', 'aux_gimbal_pitch_min',
                  'aux_gimbal_pitch_max', 'fins', 'developed', 'first_flight',
                  'illustration', 'description', 'sources']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def clean(self):
        cleaned_data = super(StageForm, self).clean()
        devel = cleaned_data.get('developed')
        flight = cleaned_data.get('first_flight')
        if wrong_year_order(devel, flight):
            raise forms.ValidationError("Things cannot fly before they are \
                                        developed")


class RocketSeriesForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = RocketSeries


class InstrumentForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Instrument
        fields = ['name', 'energy_consumption', 'description', 'illustration',
                  'sources']


class GuidanceSystemForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = GuidanceSystem
        fields = ['name', 'energy_consumption', 'description', 'illustration',
                  'sources']


class AntennaTypeForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = AntennaType


class ElectricitySourceForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = ElectricitySource


class LifeSupportTypeForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = LifeSupportType
        fields = ['name', 'energy_consumption', 'description', 'illustration',
                  'sources']


class AttitudeControlSystemForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = AttitudeControlSystem


class LandingSolutionForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = LandingSolution


class HeatshieldMaterialForm(ChemForm):

    class Meta(ChemForm.Meta):
        model = HeatshieldMaterial


class OrganizationForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Organization


class MissionTargetForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = MissionTarget


class RocketForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Rocket
        fields = ['name',  'native_name', 'country', 'variant_of',
                  'manufacturer', 'series', 'height', 'diameter', 'dry_weight',
                  'fueled_weight', 'stages', 'fairing_height', 'fairing_width',
                  'guidance_system', 'developed', 'first_flight',
                  'num_flights', 'failures', 'description', 'illustration',
                  'sources']
        widgets = None
        localized_fields = None

    def clean(self):
        cleaned_data = super(RocketForm, self).clean()
        devel = cleaned_data.get('developed')
        flight = cleaned_data.get('first_flight')
        numfly = cleaned_data.get('num_flights')
        fails = cleaned_data.get('failures')
        if wrong_year_order(devel, flight):
            raise forms.ValidationError("Things cannot fly before they are \
                                        developed")
        if fails > numfly:
            raise forms.ValidationError("Number of failures cannot exceed the \
                                        number of attempted flights")


class SpacecraftForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Spacecraft
        fields = ['name', 'native_name', 'country', 'variant_of',
                  'manufacturer', 'height', 'diameter', 'dry_weight',
                  'fueled_weight', 'instruments', 'guidance_system',
                  'antenna_type', 'antenna_gain', 'transmitter_power',
                  'attitude_control_system', 'battery_capacity',
                  'electricity_source', 'power_generation', 'tank_type',
                  'tank_material', 'fuel_volume', 'oxidizer_volume',
                  'fuel_weight', 'oxidizer_weight', 'main_engine',
                  'num_main_engines', 'aux_engine', 'num_aux_engines',
                  'heatshield', 'landing_solution', 'developed',
                  'first_flight', 'num_flights', 'failures',
                  'illustration', 'description', 'sources']
        widgets = None
        localized_fields = None

    def clean(self):
        cleaned_data = super(SpacecraftForm, self).clean()
        devel = cleaned_data.get('developed')
        flight = cleaned_data.get('first_flight')
        numfly = cleaned_data.get('num_flights')
        fails = cleaned_data.get('failures')
        if wrong_year_order(devel, flight):
            raise forms.ValidationError("Things cannot fly before they are \
                                        developed")
        if fails > numfly:
            raise forms.ValidationError("Number of failures cannot exceed the \
                                        number of attempted flights")


class CrewedSpacecraftForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = CrewedSpacecraft
        fields = ['name', 'native_name', 'country', 'variant_of',
                  'manufacturer', 'height', 'diameter', 'dry_weight',
                  'fueled_weight', 'crew', 'pressurized_volume', 'instruments',
                  'guidance_system', 'antenna_type', 'antenna_gain',
                  'transmitter_power', 'attitude_control_system',
                  'life_support', 'supplies_days', 'battery_capacity',
                  'electricity_source', 'power_generation', 'tank_type',
                  'tank_material', 'fuel_volume', 'oxidizer_volume',
                  'fuel_weight', 'oxidizer_weight', 'main_engine',
                  'num_main_engines', 'aux_engine', 'num_aux_engines',
                  'heatshield', 'landing_solution', 'developed',
                  'first_flight', 'num_flights', 'failures',
                  'illustration', 'description', 'sources']
        widgets = None
        localized_fields = None

    def clean(self):
        cleaned_data = super(CrewedSpacecraftForm, self).clean()
        devel = cleaned_data.get('developed')
        flight = cleaned_data.get('first_flight')
        numfly = cleaned_data.get('num_flights')
        fails = cleaned_data.get('failures')
        if wrong_year_order(devel, flight):
            raise forms.ValidationError("Things cannot fly before they are \
                                        developed")
        if fails > numfly:
            raise forms.ValidationError("Number of failures cannot exceed the \
                                        number of attempted flights")


class LaunchFacilityForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = LaunchFacility
        fields = ['name', 'owning_country', 'location', 'latitude',
                  'longitude', 'elevation', 'illustration', 'description',
                  'sources']
        widgets = None
        localized_fields = None


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

