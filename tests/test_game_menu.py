from src.menu import Menu, Option

def test_option_render():
  option1 = Option("[1]", "Read and load maze from file", lambda: print("Placeholder"))

  assert(option1.render() == "[1] Read and load maze from file")

def test_menu_render():
  option1 = Option("[1]", "Read and load maze from file", lambda: print("Placeholder"))
  option2 = Option("[2]", "View Maze", lambda: print("Placeholder"))
  option3 = Option("[0]", "Exit Maze", lambda: exit())
  assert()
  menu = Menu([option1, option2, option3])
  menu.render()