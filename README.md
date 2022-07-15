# Monte Carlo Simulator
Julia Burek (jeb5pb)

### Synopsis
##### Installing
```
!pip install -e .
```
```
Running setup.py develop for MonteCarloPackage
Successfully installed MonteCarloPackage-1.0.0
```

##### Importing
```
from montecarlo import Die, Game, Analyzer
```

##### Creating dice
```
Dieobject = Die([1,2,3,4])
Dieobject.faces
Dieobject.weights(2,10)
```
```
	1	2	3	4
0	1.0	10.0	1.0	1.0
```
##### Playing games
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

##### Analyzing games
- Jackpot Method
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
- Combo Method
```
die1 = Die([1,2,3,4])
die1.weights(2,10)
die2 = Die([1,2,3,4])
die2.weights(2,10)
Gameobject = Game([die1,die2])
Gameobject.play(100)
Analyzerobject.combo()
```
```

```

- Face Counts Per Roll Method
```
die1 = Die([1,2,3,4])
die1.weights(2,10)
die2 = Die([1,2,3,4])
die2.weights(2,10)
Gameobject = Game([die1,die2])
Gameobject.play(100)
Analyzerobject.faceCountsPerRoll()
```
```
	1	2	3	4
Roll 1	0	2	0	0
Roll 2	0	2	0	0
Roll 3	0	2	0	0
Roll 4	1	1	0	0
Roll 5	0	1	0	1
...	...	...	...	...
Roll 96	0	2	0	0
Roll 97	1	1	0	0
Roll 98	0	2	0	0
Roll 99	0	2	0	0
Roll 100	0	2	0
```
### API Description



### Manifest
- montecarlo.py

