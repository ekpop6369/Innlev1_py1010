# Beregning av årlige totalkostnader for elbil og bensinbil

# Antall kjørte kilometer per år /km/ 
km_per_ar = 10000

# Forsikring /kr/år/ 
forsikring_elbil = 5000
forsikring_bensinbil = 7500

# Trafikkforsikringsavgift  kr/dag
trafikkavgift_per_dag = 8.38
trafikkavgift_elbil = trafikkavgift_per_dag * 365
trafikkavgift_bensinbil = trafikkavgift_per_dag * 365

# Elbil - strøm
forbruk_elbil = 0.2          # kWh per km
strompris = 2.00             # kr per kWh
stromkostnad = km_per_ar * forbruk_elbil * strompris

# Bensinbil - drivstoff
drivstoffkostnad_bensin = km_per_ar * 1.0   # 1,0 kr per km

# Bomavgift
bom_elbil = km_per_ar * 0.1
bom_bensinbil = km_per_ar * 0.3

# Totalkostnader
totalkostnad_elbil = (
    forsikring_elbil
    + trafikkavgift_elbil
    + stromkostnad
    + bom_elbil
)

totalkostnad_bensinbil = (
    forsikring_bensinbil
    + trafikkavgift_bensinbil
    + drivstoffkostnad_bensin
    + bom_bensinbil
)

# Kostnadsdifferanse
kostnadsdifferanse = totalkostnad_bensinbil - totalkostnad_elbil

# Presentasjon av resultatene
print("Årlige kostnader")
print("-----------------------------")
print(f"Elbil:       {totalkostnad_elbil:,.2f} kr")
print(f"Bensinbil:   {totalkostnad_bensinbil:,.2f} kr")
print(f"Differanse:  {kostnadsdifferanse:,.2f} kr")