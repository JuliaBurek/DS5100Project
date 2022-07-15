# Monte Carlo Simulator
Julia Burek (jeb5pb)

## Synopsis
### Installing
```
!pip install -e .
```
```
Running setup.py develop for MonteCarloPackage
Successfully installed MonteCarloPackage-1.0.0
```

### Importing
```
from montecarlo import Die, Game, Analyzer
```

### Creating dice
```
Dieobject = Die([1,2,3,4])
Dieobject.faces
Dieobject.weights(2,10)
```
```
	1	2	3	4
0	1.0	10.0	1.0	1.0
```
### Playing games
```
die1 = Die([1,2,3,4])
die2 = Die([1,2,3,4])
Gameobject = Game([die1,die2])
Gameobject.play(10)
Gameobject.show()
```
```
	Die 1	Die 2
Roll 1	1	2
Roll 2	2	1
Roll 3	2	3
Roll 4	3	1
Roll 5	3	4
Roll 6	4	4
Roll 7	4	2
Roll 8	1	1
Roll 9	1	1
Roll 10	2	3
```

### Analyzing games
#### Jackpot Method
```
die1 = Die([1,2,3,4])
die1.weights(2,10)
die2 = Die([1,2,3,4])
die2.weights(2,10)
Gameobject = Game([die1,die2])
Gameobject.play(100)
Analyzerobject = Analyzer(Gameobject)
Analyzerobject.jackpot()
```
```
Jackpot    64
dtype: int64
```

#### Combo Method
```
die1 = Die([1,2,3,4])
die2 = Die([1,2,3,4])
Gameobject = Game([die1,die2])
Gameobject.play(10)
Analyzerobject = Analyzer(Gameobject)
Analyzerobject.combo()
```
```
		Count
Die 1	Die 2	
1	1	1
	3	1
	4	1
2	1	2
3	1	1
	2	1
4	3	1
	4	2
```

#### Face Counts Per Roll Method
```
die1 = Die([1,2,3,4])
die1.weights(2,10)
die2 = Die([1,2,3,4])
die2.weights(2,10)
Gameobject = Game([die1,die2])
Gameobject.play(10)
Analyzerobject = Analyzer(Gameobject)
Analyzerobject.faceCountsPerRoll()
```
```
	1	2	3	4
Roll 1	0	1	1	0
Roll 2	0	2	0	0
Roll 3	0	2	0	0
Roll 4	0	2	0	0
Roll 5	1	1	0	0
Roll 6	0	2	0	0
Roll 7	0	2	0	0
Roll 8	1	1	0	0
Roll 9	0	2	0	0
Roll 10	1	1	0	0
```
### API Description
#### Die Class
A die has a number of “faces” and weights, and can be rolled to select a face. The Die class takes an array of faces and initializes the weights to 1.0 for each face which can be changed. The die has one behavior, which is to be rolled one or more times.

**Methods and Attributes**
```
def __init__(self, faces):
	The init method initializes the die with an array of faces as an argument.
	It initializes the weights to 1.0 for each face and saves both faces and weights 
	to a dataframe that is used for other methods in the class.
```
- faces: array of strings or numbers
- df: dataframe of faces and weights	


```
def weights(self, face, weight):
	The weights method changes the weight of a single face. It takes a face value and weight
	value and changes the weight of the face if it is in the array of faces. 
```
- face: string or number of face to be changed
- weight: int or float of new weight


```
def roll(self, rolls=1):
	The roll method rolls the die one or more times. It returns a list of outcomes after 
	taking a random sample from the vector of faces according to their weights. The number of
	rolls defaults to 1.
```
- rolls: int (number of rolls)


```
def show(self):
	The show method displays the die's current set of faces and weights in a dataframe.
```
- df: dataframe of faces and weights



#### Game Class
A game consists of rolling one or more dice of the same kind one or more times. The Game class
takes a die object from the Die class and has a behavior to play a game. The class also keeps the 
results of its most recent play.

**Methods and Attributes**

#### Analyzer Class
An analyzer takes the results of a single game and computes various descriptive statistical properties 
about it, including face counts per roll, a jackpot count, and a combo count. The analyzer class takes 
a game object from the Game class to perform the methods on.

**Methods and Attributes**

A list of all classes with their public methods and attributes.
Each item should show their docstrings.
All paramters (with data types and defaults) should be described.
All return values should be described.
Do not describe private methods and attributes.


### Manifest
- montecarlo.py

