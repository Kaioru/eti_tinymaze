class Menu(object):
  def __init__(self, Options):
    self.Options = Options
  
  def render(self):
    for option in self.Options:
      if (option.option[1] != "0"):
        print(option.render())
      else:
        print("\n" + option.render() + "\n")
    
    return True

  def select(self, userinput):
    for option in self.Options:
      selectedOption = option.option[1]
      if (selectedOption == userinput and selectedOption != 0):
        option.function()
        self.render()
        userinput = input("Enter your option: ")
        self.select(userinput)
        return True
      elif(selectedOption == 0):
        exit()
        return True
    
class Option:
  def __init__(self, option, text, function):
    self.option = option
    self.text = text
    self.function = function

  def render(self):
    return self.option + " " + self.text
