import django_filters
from catalog.constants import COUNTRIES
from .models import Manufacturer, Compound, PropellantMix, Engine, Stage,\
    Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility, Mission, Astronaut,\
    CrewedMission


class ManufacturerFilter(django_filters.FilterSet):

    class Meta:
        model = Manufacturer
        fields = ['country', 'active']


class CompoundFilter(django_filters.FilterSet):

    class Meta:
        model = Compound
        fields = ['role', 'variety_of', 'toxicity', 'storability']


class PropellantMixFilter(django_filters.FilterSet):

    class Meta:
        model = PropellantMix
        fields = ['hypergolic', 'propellants']


class EngineFilter(django_filters.FilterSet):

    class Meta:
        model = Engine
        fields = ['country', 'manufacturer', 'application',
                  'propellants', 'cycle', 'injector_type',
                  'restart_capability']


class StageFilter(django_filters.FilterSet):

    class Meta:
        model = Stage
        fields = ['stage_role', 'main_engine', 'aux_engine', 'country',
                  'manufacturer', 'tank_type']


class RocketFilter(django_filters.FilterSet):

    class Meta:
        model = Rocket
        fields = ['country', 'series']


class SpacecraftFilter(django_filters.FilterSet):

    class Meta:
        model = Spacecraft
        fields = ['country', 'manufacturer', 'instruments',
                  'electricity_source']


class CrewedSpacecraftFilter(django_filters.FilterSet):

    class Meta:
        model = CrewedSpacecraft
        fields = ['country', 'manufacturer', 'instruments',
                  'electricity_source', 'crew']


class LaunchFacilityFilter(django_filters.FilterSet):

    class Meta:
        model = LaunchFacility
        fields = ['owning_country']


class MissionFilter(django_filters.FilterSet):

    class Meta:
        model = Mission
        fields = ['country', 'organization', 'launch_vehicle',
                  'spacecraft', 'targets', 'launch_facility', 'failure']


class CrewedMissionFilter(django_filters.FilterSet):

    class Meta:
        model = CrewedMission
        fields = ['country', 'organization', 'launch_vehicle', 'crew',
                  'spacecraft', 'targets', 'launch_facility', 'failure']


class AstronautFilter(django_filters.FilterSet):

    class Meta:
        model = Astronaut
        fields = ['nationality', 'organization']
