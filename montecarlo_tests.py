import unittest
import pandas as pd
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    # Die Class Tests
    def test_1_init(self):
        faces = [1,2,3,4,5,6]
        try:
            die = Die(faces)
        except:
            print("Initialization failed")
    
    def test_2_weights(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        die.weights(1, 5)
        test = die.df.iat[0,0]
        actual = 5
        self.assertEqual(actual, test)    
    
    def test_3_roll(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        die.weights(3, 5000)
        test = die.roll(6)
        actual = [3,3,3,3,3,3]
        self.assertEqual(actual, test)
    
    def test_4_show(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        test = die.show().shape
        actual = (1,6)
        self.assertEqual(actual, test)
    
    
    # Game Class Tests
    def test_5_init(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        try:
            game = Game([die,die,die])
        except:
            print("Initialization failed")
       
    def test_6_play(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        game = Game([die, die])
        game.play(5)
        test = game.show().shape
        actual = (5,2)
        self.assertEqual(actual, test)
    
    def test_7_show(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        game = Game([die, die])
        game.play(5)
        test = game.show(form='narrow').shape
        actual = (10,)
        self.assertEqual(actual, test)
    
    
    # Analyzer Class Tests
    def test_8_init(self):
        faces = [1,2,3,4,5,6]
        die = Die(faces)
        game = Game([die, die])
        try:
            analyzer = Analyzer(game)
        except:
            print("Initialization failed")
        
    def test_9_jackpot(self):
        faces = [1,2]
        die = Die(faces)
        die.weights(1, 100000)
        game = Game([die, die])
        game.play(2)
        analyzer = Analyzer(game)
        test = analyzer.jackpot()
        actual = 2
        self.assertEqual(actual, test)
    
    def test_10_combo(self):
        faces = [1,2,3]
        die = Die(faces)
        game = Game([die, die])
        game.play(1000)
        analyzer = Analyzer(game)
        combos = analyzer.combo()
        test = combos.shape
        actual = (9,1)
        self.assertEqual(actual, test)
    
    def test_11_faceCountsPerRoll(self):
        faces = [1,2,3]
        die = Die(faces)
        game = Game([die, die, die])
        game.play(5)
        analyzer = Analyzer(game)
        facecount = analyzer.faceCountsPerRoll()
        test = facecount.shape
        actual = (5, 3)
        self.assertEqual(actual, test)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)