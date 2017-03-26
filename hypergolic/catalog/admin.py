from django.contrib import admin
from .models import Role, StageRole, PowerCycle, Cooling, NozzleType,\
    NozzleMaterial, Injector, Manufacturer, Compound, PropellantMix, Engine,\
    TankConstruction, TankMaterial, Stage, RocketSeries, Instrument,\
    GuidanceSystem, AntennaType, ElectricitySource, LifeSupportType,\
    AttitudeControlSystem, LandingSolution, HeatshieldMaterial, Organization,\
    Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility, Mission, Astronaut,\
    CrewedMission, Igniter
# Register your models here.


@admin.register(Role)
class BasicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'illustration')


@admin.register(PropellantMix)
class PropellantMixAdmin(admin.ModelAdmin):
    filter_horizontal = ('propellants',)


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'developed', 'application',
                    'propellants', 'cycle', 'specific_impulse_vac',
                    'thrust_vac', 'twr')
    list_filter = ('application', 'propellants', 'cycle', 'injector_type',
                   'restart_capability')
    fieldsets = (
        (None, {
            'fields': ('name', 'native_name', 'application', 'country',
                       'manufacturer', 'illustration')
        }),
        ('History', {
            'fields': (('developed', 'first_flight'), 'variant_of',
                       'description')
        }),
        ('Propellants', {
            'fields': ('propellants', 'mixture_ratio', 'chamber_pressure')
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
        ('Nozzle', {
            'fields': ('nozzle_shape', 'nozzle_ratio', 'nozzle_material',
                       'cooling_method')
        }),
        ('Flexibility', {
            'fields': ('gimbal_range', 'restart_capability', 'num_restarts',
                       ('throttle_range_min', 'throttle_range_max'))
        })
    )

admin.site.register(StageRole)
admin.site.register(PowerCycle)
admin.site.register(Cooling)
admin.site.register(NozzleType)
admin.site.register(NozzleMaterial)
admin.site.register(Injector)
admin.site.register(Manufacturer)
admin.site.register(Compound)
admin.site.register(TankConstruction)
admin.site.register(TankMaterial)
admin.site.register(Stage)
admin.site.register(RocketSeries)
admin.site.register(Instrument)
admin.site.register(GuidanceSystem)
admin.site.register(AntennaType)
admin.site.register(ElectricitySource)
admin.site.register(LifeSupportType)
admin.site.register(AttitudeControlSystem)
admin.site.register(LandingSolution)
admin.site.register(HeatshieldMaterial)
admin.site.register(Organization)
admin.site.register(Rocket)
admin.site.register(Spacecraft)
admin.site.register(CrewedSpacecraft)
admin.site.register(LaunchFacility)
admin.site.register(Mission)
admin.site.register(Astronaut)
admin.site.register(CrewedMission)
admin.site.register(Igniter)
