from tkinter import *

#List of the daily tasks that must be completed

tasks = ["1H Sport", "30'' Reading", "1H Foreign languages","30'' Pictures of Earth","2H Scientific Researches"]

def check():
    if(x.get()==0):
        print("Sport: Completed! > Well done.")
    elif(x.get()==1):
        print("Reading: Completed! > Well done.")
    elif(x.get()==2):
        print("Learning foreign languages: Completed! > Well done.")
    elif(x.get()==3):
        print("Pictures: Completed! > Well done.")
    elif(x.get()==4):
        print("Science: Completed! > Well done.")
    else:
        print("YOU SUCK")
 
window = Tk()

sportImage = PhotoImage(file='sport.png')
readImage = PhotoImage(file='read.png')
languageImage = PhotoImage(file='language.png')
picturesImage = PhotoImage(file='pictures.png')
scienceImage = PhotoImage(file='science.png')

tasksImages = [sportImage,readImage,languageImage,picturesImage,scienceImage]

x = IntVar()

for index in range(len(tasks)):
    radiobutton = Radiobutton (window,
                              text=tasks[index], #add txt to button
                              variable=x, #groups radioBs together is they shared the equal variable
                              value=index,  #assigns each radioB a different value
                              padx =49, #add padding an x axis
                              font=("Impact",19),
                              image = tasksImages[index], #adds image to RadioB 
                              compound = 'left', #Position of the image
                              indicator = 0, #circle indicators
                              width =445, #Width 
                              command= check
                              )

    radiobutton.pack(anchor=W)
window.mainloop()

