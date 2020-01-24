class Menu(object):
  def __init__(self, Options, exit):
    self.Options = Options
    self.exit = exit
  
  def render(self):
    for option in self.Options:
      print(option.option + ". " + option.text)
    while (exit):
      option = input("Enter your option:")
      if (option == "1"):
        self.Options[0].function
        input("Press Enter to continue...")

      
class Option:
  def __init__(self, option, text, function):
    self.option = option
    self.text = text
    self.function = function


option1 = Option("1", "Testing", lambda: print("Do Something"))
option2 = Option("2", "This", lambda: print("Exit"))

menu = Menu([option1, option2], True)
menu.render()