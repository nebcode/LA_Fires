import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

incidents = pd.read_csv("C:\VS Code\LA_Fires\mapdataall.csv")

#southern cali counties
socal_counties = np.array([
    "Los Angeles","San Diego","Orange",
    "Riverside","San Bernardino","Ventura",
    "Santa Barbara","San Luis Obispo","Imperial",
    "Kern","Mono"
])

#standardize and replace counties
std_counties = incidents['incident_county'].str.strip().str.lower()
incidents['std_incident_county'] = std_counties
incidents.drop(columns=['incident_county'])
socal_counties = [county.strip().lower() for county in socal_counties]

#query incident df --> socal_incident df
def is_socal(county):
    return county in socal_counties
socal_incidents = incidents[incidents['std_incident_county'].apply(is_socal)]

socal_incidents = socal_incidents.drop(columns = ['incident_is_final', 'incident_date_last_update', 'incident_administrative_unit',
       'incident_administrative_unit_url',
       'incident_location', 'incident_containment',
       'incident_control', 'incident_cooperating_agencies', 'incident_type',
       'incident_url', 'incident_dateonly_extinguished', 'incident_dateonly_created',
       'is_active', 'calfire_incident', 'notification_desired',
       'std_incident_county'])
print(socal_incidents)

