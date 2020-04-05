"""
Source:
https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/
"""
import glob
import xml.etree.ElementTree as ET

# Hier werden alle Mods die derzeitig im Mod verzeichnis sind eingelesen
modOrdnerPath = "F:\\Users\\Mathias Kowitz\\Documents\\My Games\\FarmingSimulator2019\\mods\\"  # Pfad zum Mod Ordner
saveGamePath = "F:\\Users\\Mathias Kowitz\\Documents\\My Games\\FarmingSimulator2019\\savegame19\\careerSavegame.xml"  # Savegame Path

modFiles = [f for f in glob.glob(modOrdnerPath + "**/*.zip", recursive=True)]  # Mit einer List comprehension mithilfe von glob alle Dateien parsen
tmp = []

for e in modFiles:
    tmp.append(e.split('\\'))

#print(tmp[0][7][:-4])

for e in tmp:
    print(e[7][:-4])



# Hier werden die Aktiven Mods bestimmt
saveGame = ET.parse(saveGamePath)  # XML des Savegames parsen
root = saveGame.getroot()  # Die "wurzel" abspeichern
activeMods = []  # Leere Liste fuer die aktiven mods generieren

for mod in root.iter('mod'):  # Mit einer Schleife ueber die Elemente der XML gehen die "mod" im tag haben
    # print(mod.get('modName'))
    activeMods.append(mod.get('modName'))  # den Modnamen in die Liste einfuegen

# print(activeMods)

# TODO Test ob ein Element in einer anderen Liste ist
