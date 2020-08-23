print("Welcome to my first game!")
name = input("what is you name?")
age = input("What is your age?")

health = 15

print("You are starting with", health, "health")


if int(age) >= 18:

  print("You are old enough to play!")

  want_to_play = input("Do you want to play").lower()
  if want_to_play == "yes":
    print("Let's play!")

  

    left_or_right = input("First choice... Left or Right (left_or_right)?")
    if left_or_right == "left":

      ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

    if left_or_right == "right":

      ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

    if ans == "around":
     print("You went acround and reached the other side of the lake")
     

    elif ans == "across":
     print("You managed to get across, but were bit by a snake and lost 5 health. ")
     health -= 3


    ans = input("You noitce a house and a river, which do you go to (river/house)? ")

    if ans== "house":
      print("you go to the house and are greted by the owner.. She doesn't like you and you lose 5 health")
      health -= 5

      if health <= 0:
        print("You now have 0 health and you lose the game...")
      else:
          print("You have survived")

    else:
      print("You fell in the river and died...")

  else:
   print("Cool maybe next time")

elif int(age) >= 14:
  print("you can play with supervision")


else: 
  print("Your are not old enough to play...")
