print("Step Iona")
name = input("What is your name?\n")
hobby = input("Choose your favorite hobby: Gaming, photography, or coding:\n").strip().lower()
if hobby == ("Gaming").lower():
  ga = input("Are you good at gaming? Yes/No\n")
  if ga == ("Yes"):
     print("Great")
  elif ga ==("No"):
    print("Thats fine")
elif hobby == ("Photography").lower():
  pa = input("Are you good at Photography? Yes/No\n")
  if pa == ("Yes"):
    print("Great")
  elif pa ==("No"):
    print("Thats fine")
elif hobby == ("Coding").lower():
  ca = input("Are you good at Coding? Yes/No\n")
  if ca == ("Yes"):
    print("Great")
  elif ca ==("No"):
      print("Thats fine")

print("Goodbye, " + name)