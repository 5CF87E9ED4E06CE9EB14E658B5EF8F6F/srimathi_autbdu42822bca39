'''Implement a class called Player the represents a cricket Player . The player class should have a 
method called play() which prints "The Player is playing cricket   Derive two classes,  batsman and
bowler,from the Player class.  Override the play()method in each drived class to print "The batsman 
is batting " and "The bowler is bowling", respectively . write a program to create object of both the
batsman and bowler classes and call the play()method for each object .'''


#define the base class player 
class Player:
  def play(self):
    print("The player is playing cricket ")

#define the derived class batsman 
class Batsman(Player):
  def play (self):
      print("The batsman is batting")

#define the derived class bowler 
class Bowler(Player):
  def play (self):
      print("The bowler is bowling ")

#create object of batsman and bowler classes 
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object 
batsman. play()
bowler. play()
