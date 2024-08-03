class Todo:
  def __init__(dailytask, name, date):
    dailytask.name = name
    dailytask.date = date
    
  def myfunc(abc):
    print("What did you do today?: " + abc.name + abc.date)

p1 = Todo("Sport ", "> TODAY we are the")
p1.myfunc()

p1 = Todo("Read ", "> Today we are")
p1.myfunc()

p1 = Todo("Foreign language ", "> Today we are")
p1.myfunc()

p1 = Todo("Picture ", "> Today we are")
p1.myfunc()

p1 = Todo("Science ", "> Today we are")
p1.myfunc()