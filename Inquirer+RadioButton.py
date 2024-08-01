from tkinter import*

tasks = ["1H Sport", "30'' Reading", "1H Foreign languages","30'' Pictures of Earth","2H Scientific Researches"]

window = Tk()

SportImage = PhotoImage(file='Sport.png')
ReadImage = PhotoImage(file='Read.png')
LanguageImage = PhotoImage(file='Language.png')
PicturesImage = PhotoImage(file='Pictures.png')
ScienceImage = PhotoImage(file='Science.png')

x = IntVar()

for index in range(len(tasks)):
    radiobutton = Radiobutton(window,
                              text=tasks[index], #add txt to button
                              variable=x, #groups radioBs together is they shared the equal variable
                              value=index,  #assigns each radioB a different value
                              padx = 25, #add padding an x axis
                              font=("Impact",29)
                              )

    radiobutton.pack(anchor=W)
window.mainloop()

