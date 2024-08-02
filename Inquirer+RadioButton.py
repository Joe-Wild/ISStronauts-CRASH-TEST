from tkinter import *

tasks = ["1H Sport", "30'' Reading", "1H Foreign languages","30'' Pictures of Earth","2H Scientific Researches"]

def order():
    if(x.get()==0):
        print("Sport done! Well played.")
    elif(x.get()==1):
        print("Reading done! Well played.")
    elif(x.get()==2):
        print("Learning foreign languages done! played.")
    elif(x.get()==3):
        print("Pictures done! Well played.")
    elif(x.get()==4):
        print("science done! Well played.")
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
    radiobutton = Radiobutton(window,
                              text=tasks[index], #add txt to button
                              variable=x, #groups radioBs together is they shared the equal variable
                              value=index,  #assigns each radioB a different value
                              padx = 25, #add padding an x axis
                              font=("Impact",29),
                              Image = tasksImages[index], #adds image to RadioB 
                              compound = 'left', #Position of the image
                              indicator = 0, #circle indicators
                              width = 375 #Width Rb
                              )

    radiobutton.pack(anchor=W)
window.mainloop()

