from django.contrib import admin
from .models import Role, StageRole, PowerCycle, Cooling, NozzleType,\
    NozzleMaterial, Injector, Manufacturer, Compound, PropellantMix, Engine,\
    TankConstruction, TankMaterial, Stage, RocketSeries, Instrument,\
    GuidanceSystem, AntennaType, ElectricitySource, LifeSupportType,\
    AttitudeControlSystem, LandingSolution, HeatshieldMaterial, Organization,\
    Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility, Mission, Astronaut,\
    CrewedMission, Igniter, MissionTarget


@admin.register(Role, StageRole, PowerCycle, Cooling, NozzleType, Injector,
                Igniter, TankConstruction, TankMaterial, RocketSeries,
                AntennaType, ElectricitySource, AttitudeControlSystem,
                LandingSolution, Organization, MissionTarget)
class BasicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'illustration')


@admin.register(NozzleMaterial, HeatshieldMaterial)
class ChemAdmin(admin.ModelAdmin):
    list_display = ('name', 'chemical_formula', 'description', 'illustration')


@admin.register(Instrument, GuidanceSystem, LifeSupportType)
class ElectricAdmin(admin.ModelAdmin):
    list_display = ('name', 'energy_consumption', 'description',
                    'illustration')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'established', 'active', 'defunct')
    list_filter = ('country', 'active')


@admin.register(Compound)
class CompoundAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'chemical_formula', 'also_known_as',
                    'density')
    list_filter = ('role', 'variety_of', 'toxicity', 'storability')
    fieldsets = (
        (None, {
            'fields': ('name', 'chemical_formula', 'also_known_as',
                       'variety_of')
        }),
        ('Physical properties', {
            'fields': ('density', ('melting_point', 'boiling_point'))
        }),
        ('Other characteristics', {
            'fields': ('appearance', 'toxicity', 'storability', 'description',
                       'illustration', 'sources')
        })
    )


@admin.register(PropellantMix)
class PropellantMixAdmin(admin.ModelAdmin):
    filter_horizontal = ('propellants',)
    list_display = ('__str__', 'abbreviation', 'specific_impulse',
                    'optimum_ratio', 'combustion_temp')
    list_filter = ('hypergolic', 'propellants')
    list_select_related = True


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'developed', 'application',
                    'propellants', 'cycle', 'specific_impulse_vac',
                    'thrust_vac', 'twr')
    list_filter = ('country', 'manufacturer', 'application', 'propellants',
                   'cycle', 'injector_type', 'restart_capability')
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'application', 'country',
                       'manufacturer', 'variant_of', 'illustration')
        }),
        ('Performance', {
            'fields': (('specific_impulse_vac', 'specific_impulse_sl'),
                       ('thrust_vac', 'thrust_sl'),
                       ('coefficient_of_thrust_vac',
                       'coefficient_of_thrust_sl'),
                       'twr', 'rated_burn_time')
        }),
        ('Metrics', {
            'fields': ('height', 'diameter', 'dry_weight')
        }),
        ('Ignition!', {
            'fields': ('cycle', 'injector_type', 'ignition_method')
        }),
        ('Combustion', {
            'fields': ('propellants', 'mixture_ratio', 'chamber_pressure',
                       'combustion_chambers')
        }),
        ('Nozzle', {
            'fields': ('nozzle_shape', 'nozzle_ratio', 'nozzle_material',
                       'cooling_method')
        }),
        ('Flexibility', {
            'fields': ('restart_capability', 'num_restarts',
                       ('throttle_range_min', 'throttle_range_max'))
        }),
        ('History', {
            'fields': (('developed', 'first_flight'), 'description', 'sources')
        })
    )


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'developed', 'fueled_weight')
    list_filter = ('stage_role', 'main_engine', 'aux_engine', 'country',
                   'manufacturer', 'tank_type')
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'stage_role', 'country',
                       'manufacturer', 'variant_of', 'illustration')
        }),
        ('Metrics', {
            'fields': ('height', 'diameter', ('dry_weight', 'fueled_weight'))
        }),
        ('Propellant tanks', {
            'fields': ('tank_type', 'tank_material',
                       ('fuel_volume', 'oxidizer_volume'),
                       ('fuel_weight', 'oxidizer_weight'))
        }),
        ('Propulsion', {
            'fields': (('main_engine', 'num_main_engines'),
                       ('aux_engine', 'num_aux_engines'), 'burn_time')
        }),
        ('Steering', {
            'fields': (('main_gimbal_yaw_min', 'main_gimbal_yaw_max'),
                       ('main_gimbal_pitch_min', 'main_gimbal_pitch_max'),
                       ('aux_gimbal_yaw_min', 'aux_gimbal_yaw_max'),
                       ('aux_gimbal_pitch_min', 'aux_gimbal_pitch_max'),
                       'fins')
        }),
        ('History', {
            'fields': (('developed', 'first_flight'), 'description', 'sources')
        })
    )


@admin.register(Rocket)
class RocketAdmin(admin.ModelAdmin):
    filter_horizontal = ('stages',)
    list_display = ('name', 'country', 'num_stages', 'first_flight',
                    'num_flights', 'failures')
    list_filter = ('country', 'series')
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'country',
                       'manufacturer', 'series', 'variant_of', 'illustration')
        }),
        ('Metrics', {
            'fields': ('height', 'diameter', ('dry_weight', 'fueled_weight'))
        }),
        ('composition', {
            'fields': ('stages', ('fairing_height', 'fairing_width'),
                       'guidance_system')
        }),
        ('History', {
            'fields': (('developed', 'first_flight'), ('num_flights',
                       'failures'), 'description', 'sources')
        })
    )


@admin.register(Spacecraft)
class SpacecraftAdmin(admin.ModelAdmin):
    filter_horizontal = ('instruments',)
    list_display = ('name', 'country', 'first_flight', 'fueled_weight')
    list_filter = ('country', 'manufacturer', 'instruments',
                   'electricity_source')
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'country', 'manufacturer',
                       'variant_of', 'illustration')
        }),
        ('Metrics', {
            'fields': ('height', 'diameter', ('dry_weight', 'fueled_weight'))
        }),
        ('Equipment', {
            'fields': ('instruments', 'guidance_system', ('antenna_type',
                       'antenna_gain', 'transmitter_power'),
                       'attitude_control_system')
        }),
        ('Electricity', {
            'fields': (('electricity_source', 'power_generation'),
                       'battery_capacity')
        }),
        ('Propellant tanks', {
            'fields': ('tank_type', 'tank_material',
                       ('fuel_volume', 'oxidizer_volume'),
                       ('fuel_weight', 'oxidizer_weight'))
        }),
        ('Propulsion', {
            'fields': (('main_engine', 'num_main_engines'),
                       ('aux_engine', 'num_aux_engines'), 'burn_time')
        }),
        ('Landing', {
            'fields': ('heatshield', 'landing_solution')
        }),
        ('History', {
            'fields': (('developed', 'first_flight'), ('num_flights',
                       'failures'), 'description', 'sources')
        })
    )


@admin.register(CrewedSpacecraft)
class CrewedSpacecraftAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'developed', 'fueled_weight')
    list_filter = ('country', 'manufacturer', 'instruments',
                   'electricity_source')
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'country', 'manufacturer',
                       'variant_of', 'illustration')
        }),
        ('Metrics', {
            'fields': ('height', 'diameter', ('dry_weight', 'fueled_weight'),
                       'pressurized_volume')
        }),
        ('Equipment', {
            'fields': ('instruments', 'guidance_system', ('antenna_type',
                       'antenna_gain', 'transmitter_power'),
                       'attitude_control_system', 'life_support',
                       'supplies_days')
        }),
        ('Electricity', {
            'fields': (('electricity_source', 'power_generation'),
                       'batter_capacity')
        }),
        ('Propellant tanks', {
            'fields': ('tank_type', 'tank_material',
                       ('fuel_volume', 'oxidizer_volume'),
                       ('fuel_weight', 'oxidizer_weight'))
        }),
        ('Propulsion', {
            'fields': (('main_engine', 'num_main_engines'),
                       ('aux_engine', 'num_aux_engines'), 'burn_time')
        }),
        ('Landing', {
            'fields': ('heatshield', 'landing_solution')
        }),
        ('History', {
            'fields': (('developed', 'first_flight'), ('num_flights',
                       'failures'), 'description', 'sources')
        })
    )


@admin.register(LaunchFacility)
class LaunchFacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'latitude', 'longitude', 'elevation')
    list_filter = ('owning_country',)
    fieldsets = (
        (None, {
            'fields': ('name', 'owning_country')
        }),
        ('Geography', {
            'fields': ('location', 'elevation', ('latitude', 'longitude'))
        }),
        ('Other', {
            'fields': ('description', 'illustration', 'sources')
        })
    )


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    filter_horizontal = ('targets',)
    list_display = ('name', 'country', 'organization', 'launch_date',
                    'launch_facility', 'launch_vehicle', 'spacecraft',
                    'print_targets')
    list_filter = ('country', 'organization', 'launch_vehicle', 'spacecraft',
                   'targets', 'launch_facility', 'failure')
    fieldsets = (
        (None, {
            'fields': ('name', 'country', 'organization')
        }),
        ('Mission characteristics', {
            'fields': ('launch_vehicle', 'spacecraft', 'targets')
        }),
        ('History', {
            'fields': (('launch_date', 'launch_facility'),
                       ('end_date', 'failure'), 'description', 'illustration')
        })
    )


@admin.register(CrewedMission)
class CrewedMissionAdmin(admin.ModelAdmin):
    filter_horizontal = ('targets', 'crew')
    list_display = ('name', 'country', 'organization', 'launch_date',
                    'launch_facility', 'launch_vehicle', 'spacecraft',
                    'print_targets', 'print_crew')
    list_filter = ('country', 'organization', 'launch_vehicle', 'spacecraft',
                   'targets', 'launch_facility', 'failure')
    list_select_related = True
    fieldsets = (
        (None, {
            'fields': ('name', 'country', 'organization')
        }),
        ('Mission characteristics', {
            'fields': ('crew', 'launch_vehicle', 'spacecraft', 'targets')
        }),
        ('History', {
            'fields': (('launch_date', 'launch_facility'),
                       ('end_date', 'failure', 'landing_site'), 'description',
                       'illustration')
        })
    )


@admin.register(Astronaut)
class AstronautAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'organization', 'nationality', 'birth_date')
    list_filter = ('nationality', 'organization')
    fieldsets = (
        (None, {
            'fields': (('first_name', 'middle_names', 'last_name'),
                       'nationality', 'organization', 'picture')
        }),
        ('Bio', {
            'fields': (('birth_date', 'birth_place'), 'death_date',
                       'biography', 'sources')
        })
    )
