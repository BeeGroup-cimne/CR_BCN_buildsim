import pandas as pd
import json
import numpy as np

wd_buildsim = "/home/gmor/Nextcloud2/Beegroup/data/CR_BCN_buildsim"
use_case_dir = f"{wd_buildsim}/BaseCase"

# Data from CIMNE
df = pd.read_pickle(f"{wd_buildsim}/IREC_bcn_input.pkl")
df["WeatherCluster"] = "CL" + df["WeatherCluster"].astype(str)
def orientation_to_cardinal(deg):
    if (deg >= 315) or (deg < 45):
        return "north"
    elif 45 <= deg < 135:
        return "east"
    elif 135 <= deg < 225:
        return "south"
    else:
        return "west"
df["MainOrientation"] = pd.to_numeric(df["MainParcelOrientation"], errors="coerce").apply(orientation_to_cardinal)
def real_street_width_to_discrete(m):
    if m > 16:
        return '20'
    elif m > 10:
        return "12"
    else:
        return '7'
df["StreetWidth"] = pd.to_numeric(df["MainParcelOrientationStreetWidth"], errors="coerce").apply(real_street_width_to_discrete)

# Data from IREC
with open(f"{use_case_dir}/archetypes_dict.json", "r", encoding="utf-8-sig") as f:
    data = json.load(f)
    clusters = pd.DataFrame.from_dict(data).transpose()
with open(f"{use_case_dir}/building_energy_demand_yearly.json", "r", encoding="utf-8-sig") as f:
    data = json.load(f)
    clusters_demand = pd.DataFrame.from_dict(data).transpose()
clusters = clusters.join(clusters_demand)
clusters.rename(columns={
    "climate_zone": "WeatherCluster",
    "orientation": "MainOrientation",
    "street_width": "StreetWidth",
    "user_behavior": "UserBehaviour",
    "retrofitting_envelope": "RetrofittingEnvelope",
    "energy_poverty": "EnergyPoverty",
    "retrofitting_hvac": "RetrofittingHvac",
    "heating_dema_hourly_sqm": "HeatingDemand",
    "cooling_dema_hourly_sqm": "CoolingDemand",
    "dhw_dema_hourly_sqm": "DHWDemand",
    "lights_dema_hourly_sqm": "LightsDemand",
    "apps_dema_hourly_sqm": "AppliancesDemand"}, inplace=True)
clusters["SetpointHeating"] = clusters["setpoint"].str[:2]
clusters["SetpointCooling"] = clusters["setpoint"].str[2:]
clusters["BuildingType"] = clusters["archetype"].str.split("_").str[1]
clusters["YearsRange"] = clusters["archetype"].str.split("_").str[0]
def parse_years(s):
    if isinstance(s, str) and len(s) == 8 and s.isdigit():
        return int(s[:4]), int(s[4:])
    elif isinstance(s, str) and len(s) == 4 and s.isdigit():
        return np.nan, int(s)
    else:
        return np.nan, np.nan
clusters[["MinYearOfConstruction", "MaxYearOfConstruction"]] = clusters["YearsRange"].apply(
    lambda x: pd.Series(parse_years(x))
)
clusters.drop(columns=["setpoint", "archetype"], inplace=True)

#
df["YearsRange"] = ...

# Join df with the clusters results
df.join(clusters, on=["YearsRange", "WeatherCluster", "BuildingType", "StreetWidth", "MainOrientation"])
.... TODO