from django.contrib import admin
from .models import Role, StageRole, PowerCycle, Cooling, NozzleType,\
    NozzleMaterial, Injector, Manufacturer, Compound, PropellantMix, Engine,\
    TankConstruction, TankMaterial, Stage, RocketSeries, Instrument,\
    GuidanceSystem, AntennaType, ElectricitySource, LifeSupportType,\
    AttitudeControlSystem, LandingSolution, HeatshieldMaterial, Organization,\
    Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility, Mission, Astronaut,\
    CrewedMission, Igniter
# Register your models here.
admin.site.register(Spacecraft)
admin.site.register(CrewedSpacecraft)
admin.site.register(LaunchFacility)
admin.site.register(Mission)
admin.site.register(Astronaut)
admin.site.register(CrewedMission)


@admin.register(Role)
@admin.register(StageRole)
@admin.register(PowerCycle)
@admin.register(Cooling)
@admin.register(NozzleType)
@admin.register(Injector)
@admin.register(Igniter)
@admin.register(TankConstruction)
@admin.register(TankMaterial)
@admin.register(RocketSeries)
@admin.register(AntennaType)
@admin.register(ElectricitySource)
@admin.register(AttitudeControlSystem)
@admin.register(LandingSolution)
@admin.register(Organization)
class BasicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'illustration')


@admin.register(NozzleMaterial)
@admin.register(HeatshieldMaterial)
class ChemAdmin(admin.ModelAdmin):
    list_display = ('name', 'chemical_formula', 'description', 'illustration')


@admin.register(Instrument)
@admin.register(GuidanceSystem)
@admin.register(LifeSupportType)
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


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'developed', 'application',
                    'propellants', 'cycle', 'specific_impulse_vac',
                    'thrust_vac', 'twr')
    list_filter = ('country', 'manufacturer', 'application', 'propellants',
                   'cycle', 'injector_type', 'restart_capability')
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
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'stage_role', 'country',
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