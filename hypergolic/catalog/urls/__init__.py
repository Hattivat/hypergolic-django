from django.conf.urls import include, url

urlpatterns = [

    url(r'^engine_roles/', include('catalog.urls.role_urls')),  # NOQA
    url(r'^stage_roles/', include('catalog.urls.stage_role_urls')),
    url(r'^power_cycles/', include('catalog.urls.power_cycle_urls')),
    url(r'^cooling_systems/', include('catalog.urls.cooling_urls')),
    url(r'^nozzle_types/', include('catalog.urls.nozzle_type_urls')),
    url(r'^nozzle_materials/', include('catalog.urls.nozzle_material_urls')),
    url(r'^injectors/', include('catalog.urls.injector_urls')),
    url(r'^igniters/', include('catalog.urls.igniter_urls')),
    url(r'^manufacturers/', include('catalog.urls.manufacturer_urls')),
    url(r'^compounds/', include('catalog.urls.compound_urls')),
    url(r'^propellant_mixes/', include('catalog.urls.propellant_mix_urls')),
    url(r'^engines/', include('catalog.urls.engine_urls')),
    url(r'^tank_constructions/', include('catalog.urls.tank_construction_urls')),
    url(r'^tank_materials/', include('catalog.urls.tank_material_urls')),
    url(r'^stages/', include('catalog.urls.stage_urls')),
    url(r'^rocket_series/', include('catalog.urls.rocket_series_urls')),
    url(r'^instruments/', include('catalog.urls.instrument_urls')),
    url(r'^guidance_systems/', include('catalog.urls.guidance_system_urls')),
    url(r'^antenna_types/', include('catalog.urls.antenna_type_urls')),
    url(r'^electricity_sources/', include('catalog.urls.electricity_source_urls')),
    url(r'^life_support_types/', include('catalog.urls.life_support_type_urls')),
    url(r'^attitude_control_systems/', include('catalog.urls.attitude_control_system_urls')),
    url(r'^landing_solutions/', include('catalog.urls.landing_solution_urls')),
    url(r'^heatshield_materials/', include('catalog.urls.heatshield_material_urls')),
    url(r'^organizations/', include('catalog.urls.organization_urls')),
    url(r'^mission_targets/', include('catalog.urls.mission_target_urls')),
    url(r'^rockets/', include('catalog.urls.rocket_urls')),
    url(r'^spacecrafts/', include('catalog.urls.spacecraft_urls')),
    url(r'^crewed_spacecrafts/', include('catalog.urls.crewed_spacecraft_urls')),
    url(r'^launch_facilities/', include('catalog.urls.launch_facility_urls')),
    url(r'^missions/', include('catalog.urls.mission_urls')),
    url(r'^astronauts/', include('catalog.urls.astronaut_urls')),
    url(r'^crewed_missions/', include('catalog.urls.crewed_mission_urls')),
]
