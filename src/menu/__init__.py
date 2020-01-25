class Menu(object):
  def __init__(self, Options):
    self.Options = Options
  
  def render(self):
    for option in self.Options:
      if (option.option[1] != "0"):
        print(option.option + " " + option.text)
      else:
        print("\n" + option.option + " " + option.text + "\n")

    userinput = input("Enter your option: ")

    for option in self.Options:
      if (option.option[1] == userinput):
        option.function()
    
    input("Press Enter to continue...")
    
    self.render()

      
class Option:
  def __init__(self, option, text, function):
    self.option = option
    self.text = text
    self.function = function
