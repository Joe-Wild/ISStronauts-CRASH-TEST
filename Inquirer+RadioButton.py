from tkinter import*

tasks = ["1H Sport", "30'' Reading", "1H Foreign languages","30'' Pictures of Earth","2H Scientific Researches"]

window = Tk()

SportImage = PhotoImage(file='sport.png')
ReadImage = PhotoImage(file='read.png')
LanguageImage = PhotoImage(file='language.png')
PicturesImage = PhotoImage(file='pictures.png')
ScienceImage = PhotoImage(file='science.png')

x = IntVar()

for index in range(len(tasks)):
    radiobutton = Radiobutton(window,
                              text=tasks[index], #add txt to button
                              variable=x, #groups radioBs together is they shared the equal variable
                              value=index,  #assigns each radioB a different value
                              padx = 25, #add padding an x axis
                              font=("Impact",29),
                              image = tasksimages[index], #adds image to RadioB 
                              compound = 'left'#Position of the image
                              )

    radiobutton.pack(anchor=W)
window.mainloop()

