from django.db import models

# Create your models here.
YEARS = [(1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924),
        (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929),
        (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934),
        (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939),
        (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944),
        (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949),
        (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954),
        (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959),
        (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964),
        (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969),
        (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974),
        (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979),
        (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984),
        (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989),
        (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994),
        (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999),
        (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004),
        (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009),
        (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014),
        (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019),
        (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024),
        (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029),
        (2030, 2030)]

DEGREES = [("very low", "very low"), ("low", "low"), ("medium", "medium"),
            ("high", "high"), ("very high", "very high")]

class Role(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='engineroles/')

class StageRole(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='stageroles/')

class PowerCycle(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='powercycles/')

class Cooling(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='coolingmethods/')

class NozzleType(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='nozzletypes/')

class NozzleMaterial(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    chemical_formula = models.CharField(max_leght=30, blank=True)
    illustration = models.ImageField(blank=True, upload_to='nozzlematerials/')

class Injector(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='injectors/')

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    native_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    established = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    active = models.BooleanField(blank=True)
    defunct = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    headquarters = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to='manufacturers/')

class Compound(models.Model):
    name = models.CharField(max_lenght=100, primary_key=True, unique=True)
    role = models.BooleanField() # true = fuel, false = oxidizer
    chem_formula = models.CharField(max_length=30)
    density = models.FloatField()
    melting_point = models.DecimalField(max_digits=6, decimal_places=2) # in degrees Celsius
    boiling_point = models.DecimalField(max_digits=6, decimal_places=2) # in degrees Celsius
    appearance = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(max_length=20, choices=DEGREES, blank=True)
    storability = models.CharField(max_length=20, choices=DEGREES, blank=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='chemcompounds/')

class FuelOxidizerMix(models.Model):
    fuel = models.ForeignKey(Compound, on_delete=models.CASCADE,
                                limit_choices_to={'role': True})
    oxidizer = models.ForeignKey(Compound, on_delete=models.CASCADE, null=True,
                                limit_choices_to={'role': False}, blank=True)
    hypergolic = models.BooleanField()
    specific_impulse = models.PositiveIntegerField() # stored in m/s
    specific_impulse_sl = models.PositiveIntegerField(blank=True) # stored in m/s
    optimum_ratio = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    combustion_temp = models.DecimalField(max_digits=6, decimal_places=1, blank=True)
    description = models.TextField(blank=True)

class Engine(models.Model):
    name = models.CharField(max_length=50)
    variant_of = models.ForeignKey('self', on_delete=models.SET_NULL,
                                    blank=True, null=True)
    native_name = models.CharField(max_length=50, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    application = models.ForeignKey(Role, on_delete=models.SET_NULL,
                                    blank=True, null=True)
    propellants = models.ForeignKey(FuelOxidizerMix, on_delete=models.PROTECT)
    mixture_ratio = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    cycle = models.ForeignKey(PowerCycle, on_delete=models.SET_NULL,
                                blank=True, null=True)
    specific_impulse_vac = models.PositiveIntegerField() # stored in m/s
    specific_impulse_sl = models.PositiveIntegerField() # stored in m/s
    thrust_sl = models.PositiveIntegerField() # stored in newtons
    thrust_vac = models.PositiveIntegerField() # stored in newtons
    twr = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    chamber_pressure = models.PositiveIntegerField(blank=True) # stored in pascals
    rated_burn_time = models.PositiveSmallIntegerField(blank=True) # in seconds
    nozzle_ratio = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    nozzle_shape = models.ForeignKey(NozzleType, on_delete=models.PROTECT,
                                        blank=True, null=True)
    nozzle_material = models.ForeignKey(NozzleMaterial, on_delete=models.PROTECT,
                                        blank=True, null=True)
    cooling_method = models.ForeignKey(Cooling, on_delete=models.PROTECT,
                                        blank=True, null=True)
    injector_type = models.ForeignKey(Injector, on_delete=models.PROTECT,
                                        blank=True, null=True)
    height = models.PositiveIntegerField(blank=True) # stored in milimeters
    diameter = models.PositiveIntegerField(blank=True) # stored in milimeters
    weight_dry = models.PositiveIntegerField(blank=True) # stored in grams
    gimbal_range = models.DecimalField(max_digits=4, decimal_places=1, blank=True)
    coefficient_of_thrust_vac = models.FloatField(blank=True)
    coefficient_of_thrust_sl = models.FloatField(blank=True)
    ignition_method = models.CharField(blank=True)
    restart_capability = models.BooleanField(default=False)
    num_restarts = models.PositiveSmallIntegerField(default=0, blank=True)
    throttle_range_min = models.PositiveSmallIntegerField(default=100, blank=True)
    throttle_range_max = models.PositiveSmallIntegerField(default=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='engines/')

class TankConstruction(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='constructiontypes/')

class TankMaterial(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    description = models.TextField(blank=True)
    illustration = models.ImageField(blank=True, upload_to='tankmaterials/')

class Stage(models.Model):
    name = models.CharField(max_length=50)
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    empty_mass = models.PositiveIntegerField() # stored in grams
    fueled_mass = models.PositiveIntegerField() # stored in grams
    main_engine = models.ForeignKey(Engine, on_delete=models.PROTECT)
    num_main_engines = models.PositiveSmallIntegerField(default=1)
    aux_engine = models.ForeignKey(Engine, on_delete=models.PROTECT, blank=True)
    num_aux_engines = models.PositiveSmallIntegerField(blank=True, default=0)
    height = models.PositiveIntegerField() # stored in milimeters
    diameter = models.PositiveIntegerField() # stored in milimeters
    tank_type = models.ForeignKey(TankConstruction, on_delete=models.SET_NULL, blank=True, null=True)
    tank_material = models.ForeignKey(TankMaterial, on_delete=models.SET_NULL, blank=True, null=True)
    burn_time = models.PositiveIntegerField(blank=True) # in seconds
    image = models.ImageField(blank=True, upload_to='stages/')

class RocketSeries(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='rocketseries/')

class Rocket(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, blank=True)
    variant_of = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    series = models.ForeignKey(RocketSeries, on_delete=models.PROTECT, blank=True)
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    stages = models.ManyToManyField(Stage)
    num_flights = models.PositiveSmallIntegerField(default=0)
    failures = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(blank=True, upload_to='rockets/')

class Spacecraft(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, blank=True)
    variant_of = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    developed = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    first_flight = models.PositiveSmallIntegerField(choices=YEARS, blank=True)
    height = models.PositiveIntegerField() # stored in milimeters
    diameter = models.PositiveIntegerField() # stored in milimeters
    empty_mass = models.PositiveIntegerField(blank=True) # stored in grams
    fueled_mass = models.PositiveIntegerField(blank=True) # stored in grams

