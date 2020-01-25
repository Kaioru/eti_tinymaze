from src.menu import Menu, Option


menu = Menu([
    Option("1", "Read and load maze from file", lambda: None),
    Option("2", "View maze", lambda: None),
    Option("3", "Play maze game", lambda: None),
    Option("4", "Configure current maze", lambda: None),
    Option("5", "Exit maze", lambda: None),
])
print(menu.render())

selection = input("Enter your option: ")
menu.select(selection)