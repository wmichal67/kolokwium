import pomiary

temp_f = pomiary.c_to_f(25)
kmps = pomiary.predkosc_wiatru(10)
mmHg = pomiary.cisnienie_atmosferyczne(1013)
print(f"Przeliczając 25°C na Fahrenheita to: {temp_f}")
print(f"Przekształcając prędkość wiatru 10 m/s to {kmps} km/h")
print(f"Przekształcając ciśnienie atmosferyczne 1013 hPa to {mmHg} w mmHg.")

#Efekt 2
dane_pogodowe = [
    {"temp": 20, "wiatr": 5, "cisnienie": 1000},
    {"temp": 22, "wiatr": 7, "cisnienie": 1012},
    {"temp": 18, "wiatr": 6, "cisnienie": 995}
]
cisnienia_mmHg = [pomiary.cisnienie_atmosferyczne(dzien["cisnienie"])
for dzien in dane_pogodowe]
srednie_cisnienie = sum(cisnienia_mmHg) / len(cisnienia_mmHg)

print(f"Średnie ciśnienie atmosferyczne z 3 dni: {srednie_cisnienie:.2f} mmHg")