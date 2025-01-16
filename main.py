#Day 7
print("Let's test if you are a true fan of Suits")
print("---")
lawyer = input("Did Suits make you consider, even a little, to change your profession to being a lawyer?: ")
if lawyer == "Yes":
  favouriteCharacter = input("Who is your favourite character from Suits?: ")
  if favouriteCharacter in ["Harvey", "Donna", "Mike", "Rachel", "Louis", "Samantha", "Katrina", "Robert", "Dana", "Alex"]:
    finishSeries = input("Did you finish the whole Suits series?: ")
    if finishSeries == "Yes":
      print("True fan! Welcome to the Suits fan club!")
    else:
      print("Fake fan!")
  else:
    print("Fake fan!")
else:
  print("Fake fan!")