# CR_BCN_buildsim

Welcome to the **CR_BCN_buildsim** repository.

This repository contains scripts, models, and data workflows to simulate the thermal energy demand of approximately 37,000 residential buildings in Barcelona. The simulation engine is based on Reduced Order Grey Box Models (RC models) calibrated with white box TRNSYS simulations, allowing building-level predictions for heating, cooling, and total energy needs under different climate, geometry, and retrofit scenarios.


The data required is stored in the NextCloud repository managed by our department at CIMNE.

---

## 📌 Authors

- Jose Manuel Broto - jmbroto@cimne.upc.edu
- Maria Teresa Sellart - tsellart@cimne.upc.edu
- Gerard Mor - gmor@cimne.upc.edu
- Aggelos Mylonas - amylonas@irec.cat
- Enric Mont Lecocq - emont@irec.cat
- Jordi Pascual - jpascual@irec.cat

---

## 🎯 Project Objectives

To simulate the final and primary energy consumption, CO₂ emissions, and economic costs associated with HVAC systems for all buildings under both:

- Base case (current conditions)
- Retrofitted and decarbonized scenarios

---

## 📁 Scripts Overview

---

## 📊 Datasets Used

---

## 🏗️ Modelling Methodology

### White Box Simulations (TRNSYS)

Used to calibrate the reduced-order models. Based on:

- **3 building geometries:**
	- Multi-Family Isolated (MFI)
	- Multi-Family Non-Isolated (MFNI)
	- Single Family (SF)

- **17 original archetypes by construction period**
	- BA_1900_MFNI
	- BA_19011940_MFNI
	- BA_19011940_SF
	- BA_19411960_MFI
	- BA_19411960_MFNI
	- BA_19411980_SF
	- BA_19611980_MFI
	- BA_19611980_MFNI
	- BA_19812007_MFNI
	- BA_19812019_SF
	- BA_20082014_MFNI
	- BA_20152019_MFNI
	- BA_1900_MFI
	- BA_19011940_MFI
	- BA_19812007_MFI 
	- BA_20082014_MFI 
	- BA_20152025_MFI


Hourly resolution outputs from TRNSYS include:

- Indoor temperature (Ti)
- Wall temperature (Tw)
- Ambient temperature (Tamb)
- Solar radiation (Ir)
- Internal gains/losses (Qin)
- Heating and cooling demand (Q)

---

### Grey Box Models (RC – Reduced Order)

Grey box models use the **R2C2 state-space approach**, simulating thermal dynamics via a **lumped resistance and capacitance** electric analog.

- Parameters are **calibrated vs. white box results**  
- Allows **fast, large-scale computation**  
- Models adapted where needed to match new building archetypes

---

## 📈 Simulation Parameters

Each building is defined by a unique combination of parameters stored in:

### `Base_case_archetypes_dict`

A dictionary containing 9 configuration fields:

| Key | Description |
|-----|-------------|
| `setpoint` | `"2226"` – Heating: 22 °C, Cooling: 26 °C |
| `archetype` | `"PeriodoConstructivo_MFI/MFNI/SF"` – Construction period + geometry |
| `climate_zone` | `"CL0"` to `"CL4"` – Weather clusters for Barcelona |
| `orientation` | One of 4 main cardinal directions |
| `street_width` | `"7"`, `"12"`, or `"20"` – Distance to opposite facade (in meters) |
| `user_behavior` | `"unaware"` – User not actively managing energy use |
| `retrofitting_envelope` | `"no"` or `"3"` – If building was renovated (windows + facade), based on year |
| `retrofitting_hvac` | `"no"` or `"heatpump"` – Added if building was renovated from 2015 onwards |
| `energy_poverty` | `"no"` – Not considered in this project |


> **Note:** While the base case only uses the `"2226"` configuration (Heating: 22 °C, Cooling: 26 °C),  
> the simulation framework supports the following combinations of heating/cooling setpoints:

| Heating [°C] | Cooling [°C] |
|--------------|--------------|
| 15           | 30           |
| 19           | 29           |
| 20           | 28           |
| 21           | 27           |
| 22           | 26           |

---

## 🔁 Renovation Scenarios

### Envelope Renovation

| Label | Intervention |
|-------|--------------|
| `no` | No retrofitting considered |
| `3`  | Windows + façade |

### HVAC Retrofitting

| Label | Intervention |
|-------|--------------|
| `no` | No HVAC changes |
| `heatpump` | Adds heat pump system (from 2015+) |


---

## 📊 Output Data

The results are saved in two aggregated files that contain data for **all simulated buildings**:

### `Building_energy_demand_yearly`

- Heating demand [kWh/m²/year]  
- Cooling demand [kWh/m²/year]  
- Domestic Hot Water (DHW) [kWh/m²/year]  
- Lighting and appliances [kWh/m²/year]  

> All values are normalised per square meter.

---

### `Kpis_yearly`

A complete set of **Key Performance Indicators** (KPIs). Includes:

- Final energy by vector  
- Primary energy  
- CO₂ emissions  
- Energy cost per use  
- Total energy cost  

> KPIs related to **biomass** are always set to `0`, as **biomass is not considered** in the Barcelona context.

---

## 📜 License

This project is licensed under the **European Union Public License (EUPL), Version 1.2**.  
You may obtain a copy of the license at:

[https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12)

Unless required by applicable law or agreed to in writing, software distributed under this license is distributed **on an "AS IS" basis**, without warranties or conditions of any kind.

©  2024 Maria Teresa Sellart, Jose Manuel Broto, Gerard Mor

---


Thank you for using **CR_BCN_meteo**!  
For any questions or suggestions, feel free to reach gmor@cimne.upc.edu
