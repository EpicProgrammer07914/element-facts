#pip install termcolored
#pip install selenuim and put chrome driver from chronuim in path, download it here: https://chromedriver.chromium.org/downloads

from selenium import webdriver
from termcolor import colored

#
elements = """Hydrogen 
Helium, Lithium, Beryllium, Boron, Carbon, NitrogenOxygen, Fluorine, Neon, Sodium,
Magnesium, Aluminum, Silicon, Phosphorus, Sulfur, Chlorine, Argon, Potassium, Calcium, Scandium, Titanium, Vanadium, Chromium,
Manganese, Iron Cobalt, Nickel, Copper, Zinc Gallium, Germanium, Arsenic, Selenium, Bromine, Krypton, Rubidium, Strontium, Yttrium,
Zirconium, Niobium, Molybdenum, Technetium, Ruthenium, Rhodium, Palladium, Silver, Cadmium, Indium, Tin, Antimony, Tellurium, Iodine, Xenon, Cesium,
Barium, Lanthanum, Cerium, Praseodymium, Neodymium, Promethium, Samarium, Europium, Gadolinium, Terbium, Dysprosium,
Holmium, Erbium, Thulium, YtterbiumLutetium, Hafnium, Tantalum, Tungsten, Rhenium, Osmium, Iridium, Platinum, Gold, Mercury,
Thallium, Lead, Bismuth, Polonium, Astatine, Radon, Francium, Radium, Actinium, Thorium, Protactinium, Uranium,
Neptunium, Plutonium, Americium, Curium, Berkelium, Californium, Einsteinium, Fermium, Mendelevium, Nobelium, Lawrencium, Rutherfordium, Dubnium, 
Seaborgium, Bohrium, Hassium, Meitnerium, Darmstadtium, Roentgenium, Copernicium, Nihonium, Flerovium, Moscovium, Livermorium, Tennessine, Oganesson"""
print(colored(elements, 'yellow'))
print(colored("copy and paste whatever element you want to know about! ", 'green'))
#

print(" ")
inputt = str(input("what element would you like to know about: "))

if inputt == ",":
	print("element not found. error 404")

elif inputt in elements:
	#https://www.google.com/search?q=what+is+titanium&rlz=1C1CHBF_enUS926US927&oq=what+is+&aqs=chrome.0.69i59l2j69i57j69i59j0i67j0i131i433j0j69i61.1391j0j7&sourceid=chrome&ie=UTF-8
	inputt = "facts+about+" + inputt
	loink = "https://www.google.com/search?q=" + inputt + "&rlz=1C1CHBF_enUS926US927&oq=" + inputt + "&aqs=chrome..69i57j69i59l3j69i60j69i61l3.562j0j7&sourceid=chrome&ie=UTF-8"
	print(loink)

	driver = webdriver.Chrome(r'C:\Users\naras\Downloads\chromedriver_win32 (1)\chromedriver.exe')
	driver.get(loink)
else:
	print("element not found. error 404")
