class Tasks:
  def __init__(dailytask, name, date):
    dailytask.name = name
    dailytask.date = date
    
  def myfunc(abc):
    print("You managed to accomplish " + abc.name + abc.date)

p1 = Tasks("Sport on ", " /  /  ")
p1.myfunc()

p1 = Tasks("Read on ", "  /  /  ")
p1.myfunc()

p1 = Tasks("Foreign language on ", "  /  /  ")
p1.myfunc()

p1 = Tasks("Picture on", "  /  /  ")
p1.myfunc()

p1 = Tasks("Science on ", "  /  /  ")
p1.myfunc()


