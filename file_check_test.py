"""
Source:
https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
"""
import glob
import xml.etree.ElementTree as ET
import file_paths as mod_paths


modFiles = [f for f in glob.glob(mod_paths.modOrdnerPath + "**/*.zip", recursive=True)]  # Mit einer List comprehension mithilfe von glob alle Dateien parsen
modNames = []

for e in modFiles:
    modNames.append(e.split('\\')[7][:-4])

# Hier werden die Aktiven Mods bestimmt
saveGame = ET.parse(mod_paths.saveGamePath)  # XML des Savegames parsen
root = saveGame.getroot()  # Die "wurzel" abspeichern
activeMods = []  # Leere Liste fuer die aktiven mods generieren

for mod in root.iter('mod'):  # Mit einer Schleife ueber die Elemente der XML gehen die "mod" im tag haben
    # print(mod.get('modName'))
    activeMods.append(mod.get('modName'))  # den Modnamen in die Liste einfuegen

# Test ob ein Element in einer anderen Liste ist
for mod in modNames:
    if mod in activeMods:
        print("Die Mod: " + mod + " gehoert in den Spielstand.")
    else:
        print("Die Mod: " + mod + " gehoert NICHT in den Spielstand.")

print("")
print("Mods insgesamt im Ordner: " + str(len(modNames)))
print("Mods insgesamt im Spielstand aktiviert: " + str(len(activeMods)))
