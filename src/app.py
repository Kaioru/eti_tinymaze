from menu import Menu, Option

 
option1 = Option("[1]", "Read and load maze from file", lambda: print("Placeholder"))
option2 = Option("[2]", "View maze", lambda: print("Placeholder"))
option3 = Option("[3]", "Play maze game", lambda: print("Placeholder"))
option4 = Option("[4]", "Configure current maze", lambda: print("Placeholder"))
option5 = Option("[0]", "Exit Maze", lambda: exit())

menu = Menu([option1, option2, option3, option4, option5])
menu.render()
userinput = input("Enter your option: ")
menu.select(userinput)
