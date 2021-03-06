from django.shortcuts import render
from .role_views import *  # NOQA
from .stage_role_views import *  # NOQA
from .power_cycle_views import *  # NOQA
from .cooling_views import *  # NOQA
from .nozzle_type_views import *  # NOQA
from .nozzle_material_views import *  # NOQA
from .injector_views import *  # NOQA
from .igniter_views import *  # NOQA
from .manufacturer_views import *  # NOQA
from .compound_views import *  # NOQA
from .propellant_mix_views import *  # NOQA
from .engine_views import *  # NOQA
from .tank_construction_views import *  # NOQA
from .tank_material_views import *  # NOQA
from .stage_views import *  # NOQA
from .rocket_series_views import *  # NOQA
from .instrument_views import *  # NOQA
from .guidance_system_views import *  # NOQA
from .antenna_type_views import *  # NOQA
from .electricity_source_views import *  # NOQA
from .life_support_type_views import *  # NOQA
from .attitude_control_system_views import *  # NOQA
from .landing_solution_views import *  # NOQA
from .heatshield_material_views import *  # NOQA
from .organization_views import *  # NOQA
from .mission_target_views import *  # NOQA
from .rocket_views import *  # NOQA
from .spacecraft_views import *  # NOQA
from .crewed_spacecraft_views import *  # NOQA
from .launch_facility_views import *  # NOQA
from .mission_views import *  # NOQA
from .astronaut_views import *  # NOQA
from .crewed_mission_views import *  # NOQA


def home(request):
    return render(request, 'catalog/home.html')
