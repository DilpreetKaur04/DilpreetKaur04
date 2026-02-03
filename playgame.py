def show_welcome_menu():
  print("Welcome to an escape room!")
  print("You will be asked to make choices.")
  print("Press Enter to see the choices...")
  input()

def show_choices():
  print("Our Games are: ")
  print("1. The Crazy Cat Lady")
  print("2. Escape the Night")
  choice = input("Enter 1 or 2: ")
  if choice == "1":
    print("You chose The Crazy Cat Lady")
  elif choice == "2":
    print("You chose Escape the Night")
  else:
    print("Invalid choice")
    return choice
  
def game1():
  print("Welcome to The Crazy Cat Lady")
  print("You see a cat and a room.")
  option = input("Do you pet the cat or go to the room? ")
  print("Your option is - ", option)
  if option == "pet":
    print("PET")
    print("The cat likes you. You win!")
  elif option == "room":
    print("ROOM")
    print("The door is locked. Try again!")
  else:
    print("Oops")
    print("Invalid option.")

def game2():
    print("Welcome to Escape the Night")
    print("You are in a dark room.")
    print("There is a torch and a door.")
    option = input("Do you take the torch or open the door? ")
    print("Your option is - ", option)
    if option == "torch":
      print("TORCH")
      print("The room lights up and you escape safely!")
    elif option == "door":
      print("DOOR")
      print("It’s too dark… you are still trapped")
    else:
      print("Oops")
      print("Invalid option.")
  
def play_game(choice):
  if choice == "1":
    game1()
  elif choice == "2":
    game2()
  else:
    print("Oops")
    print("Invalid choice. Exiting game.")

show_welcome_menu()
choice = show_choices()
play_game(choice)
