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
## API Description
### Die Class
A die has a number of “faces” and weights, and can be rolled to select a face. The Die class takes an array 
of faces and initializes the weights to 1.0 for each face which can be changed. The die has one behavior, 
which is to be rolled one or more times.

#### Methods and Attributes
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



### Game Class
A game consists of rolling one or more dice of the same kind one or more times. The Game class
takes a die object from the Die class and has a behavior to play a game. The class also keeps the 
results of its most recent play.

#### Methods and Attributes
```
    def __init__(self, die_obj):
        The init method initializes a die object from the Die class and an empty dataframe to be used in the other methods.
```
- die_obj:
- gamedf: 


```
    def play(self, x):
        The play method takes a parameter of how many times the dice should be rolled and saves the result of the 
	play to a dataframe. 
```
- x: int (number of rolls)
- .roll(): roll function from Die class 
- gamedf: dataframe of rolls and die objects


```
    def show(self, form = 'wide'):
        The show method passes the dataframe to the user. It takes a parameter to return the dataframe in narrow or 
	wide form, the default form.
```
- form: string ('narrow' or 'wide')
- 

### Analyzer Class
An analyzer takes the results of a single game and computes various descriptive statistical properties 
about it, including face counts per roll, a jackpot count, and a combo count. The analyzer class takes 
a game object from the Game class to perform the methods on.

#### Methods and Attributes
```
def __init__(self, game_obj):
        The init method takes a game object from the Game class as its input parameter and infers the data 
	type of the die faces used.
```
- game_obj:


```
    def jackpot(self):
        The jackpot method computes how many times the game resulted in all faces being identical. It returns an 
	integer for the number of jackpots and stores the results in a dataframe.
```
- jackpotdf:


```
def combo(self):
        The combo method computes the distinct combinations of faces rolled, along with their counts. Combinations are 
	sorted and and saved as a multi-columned index.
```
-
-


```
 def faceCountsPerRoll(self):
        The faceCountsPerRoll method computes how many times a given face is rolled in each event. It stores the 
	results as a dataframe that has an index of the roll number and face values as columns.
```
-
-



### Manifest
- README.md
- montecarlo.py
- montecarlo_tests.py
- montecarlo_tests.txt
- FinalProjectSubmissionTemplate.ipynb
- setup.py
- __init__.py

