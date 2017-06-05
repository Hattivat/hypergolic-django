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
                  'specific_impulse', 'characteristic_velocity',
                  'optimum_ratio', 'combustion_temp', 'description', 'sources']


class EngineForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Engine
        fields = ['name', 'native_name', 'application', 'country',
                  'manufacturer', 'variant_of', 'specific_impulse_vac',
                  'specific_impulse_sl', 'thrust_vac', 'thrust_sl', 'twr',
                  'coefficient_of_thrust_vac', 'coefficient_of_thrust_sl',
                  'rated_burn_time', 'height', 'diameter', 'dry_mass',
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
        restarts = cleaned_data.get('num_restarts')
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
                  'manufacturer', 'height', 'diameter', 'dry_mass',
                  'fueled_mass', 'tank_type', 'tank_material', 'fuel_volume',
                  'oxidizer_volume', 'fuel_mass', 'oxidizer_mass',
                  'main_engine', 'burn_time', 'num_main_engines', 'aux_engine',
                  'num_aux_engines', 'aux_fuel_volume', 'aux_oxidizer_volume',
                  'aux_fuel_mass', 'aux_oxidizer_mass', 'pressurant',
                  'main_gimbal_yaw_min', 'main_gimbal_yaw_max',
                  'main_gimbal_pitch_min', 'main_gimbal_pitch_max',
                  'aux_gimbal_yaw_min', 'aux_gimbal_yaw_max',
                  'aux_gimbal_pitch_min', 'aux_gimbal_pitch_max', 'fins',
                  'developed', 'first_flight', 'illustration', 'description',
                  'sources']
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
        fields = ['name', 'native_name', 'country', 'variant_of',
                  'manufacturer', 'series', 'height', 'diameter', 'dry_mass',
                  'fueled_mass', 'stages', 'fairing_height', 'fairing_width',
                  'fairing_mass', 'guidance_system', 'battery_capacity',
                  'payload_to_leo', 'payload_to_gto', 'payload_to_tli',
                  'developed', 'first_flight', 'num_flights', 'failures',
                  'description', 'illustration', 'sources']
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
                  'manufacturer', 'height', 'diameter', 'dry_mass',
                  'fueled_mass', 'instruments', 'guidance_system',
                  'antenna_type', 'antenna_gain', 'transmitter_power',
                  'attitude_control_system', 'battery_capacity',
                  'electricity_source', 'power_generation', 'tank_type',
                  'tank_material', 'fuel_volume', 'oxidizer_volume',
                  'fuel_mass', 'oxidizer_mass', 'main_engine',
                  'num_main_engines', 'aux_engine', 'num_aux_engines',
                  'aux_fuel_volume', 'aux_oxidizer_volume',
                  'aux_fuel_mass', 'aux_oxidizer_mass', 'pressurant',
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
                  'manufacturer', 'height', 'diameter', 'dry_mass',
                  'fueled_mass', 'crew', 'pressurized_volume', 'instruments',
                  'guidance_system', 'antenna_type', 'antenna_gain',
                  'transmitter_power', 'attitude_control_system',
                  'life_support', 'supplies_days', 'battery_capacity',
                  'electricity_source', 'power_generation', 'tank_type',
                  'tank_material', 'fuel_volume', 'oxidizer_volume',
                  'fuel_mass', 'oxidizer_mass', 'main_engine',
                  'num_main_engines', 'aux_engine', 'num_aux_engines',
                  'aux_fuel_volume', 'aux_oxidizer_volume',
                  'aux_fuel_mass', 'aux_oxidizer_mass', 'pressurant',
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


class MissionForm(BasicForm):

    class Meta(BasicForm.Meta):
        model = Mission
        fields = ['name', 'country', 'organization', 'launch_vehicle',
                  'spacecraft', 'targets', 'launch_date', 'launch_facility',
                  'end_date', 'failure', 'illustration', 'description',
                  'sources']
        widgets = None
        localized_fields = None

    def clean(self):
        cleaned_data = super(MissionForm, self).clean()
        launch = cleaned_data.get('launch_date')
        end = cleaned_data.get('end_date')
        if launch > end:
            raise forms.ValidationError("End date cannot be earlier than the\
                                        launch date")


class AstronautForm(forms.ModelForm):

    class Meta:
        model = Astronaut
        fields = ['first_name', 'middle_names', 'last_name', 'nationality',
                  'organization', 'birth_date', 'birth_place', 'death_date',
                  'picture', 'biography', 'sources']
        widgets = None
        localized_fields = None

    def clean(self):
        cleaned_data = super(AstronautForm, self).clean()
        born = cleaned_data.get('birth_date')
        died = cleaned_data.get('death_date')
        if born > died:
            raise forms.ValidationError("Death date cannot be earlier than the\
                                        birth date")


class CrewedMissionForm(forms.ModelForm):

    class Meta(BasicForm.Meta):
        model = CrewedMission
        fields = ['name', 'country', 'organization', 'crew', 'launch_vehicle',
                  'spacecraft', 'targets', 'launch_date', 'launch_facility',
                  'end_date', 'failure', 'landing_site', 'description',
                  'illustration', 'sources']
        widgets = None
        localized_fields = None

    def clean(self):
        cleaned_data = super(CrewedMissionForm, self).clean()
        launch = cleaned_data.get('launch_date')
        end = cleaned_data.get('end_date')
        if launch > end:
            raise forms.ValidationError("End date cannot be earlier than the\
                                        launch date")
