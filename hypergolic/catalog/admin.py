from django.contrib import admin
from .models import Role, StageRole, PowerCycle, Cooling, NozzleType,\
    NozzleMaterial, Injector, Manufacturer, Compound, FuelOxidizerMix, Engine,\
    TankConstruction, TankMaterial, Stage, RocketSeries, Instrument,\
    GuidanceSystem, AntennaType, ElectricitySource, LifeSupportType,\
    AttitudeControlSystem, LandingSolution, HeatshieldMaterial, Organization,\
    Rocket, Spacecraft, CrewedSpacecraft, LaunchFacility, Mission, Astronaut,\
    CrewedMission, Igniter
# Register your models here.

admin.site.register(Role)
admin.site.register(StageRole)
admin.site.register(PowerCycle)
admin.site.register(Cooling)
admin.site.register(NozzleType)
admin.site.register(NozzleMaterial)
admin.site.register(Injector)
admin.site.register(Manufacturer)
admin.site.register(Compound)
admin.site.register(FuelOxidizerMix)
admin.site.register(Engine)
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
