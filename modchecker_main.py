try:
    from tkinter import *
except ImportError as error:
    print(error)
    print("Something went wrong when importing the Tkinter Module")

root = Tk()
root.title("Farming Simulator 19 - Modchecker")  # Fenstertitel
root.geometry("1000x900+300+50")  # Neues fenster 1000x 900y erstellen an position 300x 50y


for savegame in range(1, 50):  # Fake Data erstellen, zum testen
    newLabel = Label(root, text="Savegame " + str(savegame)).grid(row=savegame, column=0)
    # TODO Herausfinden wie man die scrollbar sinnvoll integriert. Das wird wichtig bei Modlisten die sehr lang sind

root.mainloop()
