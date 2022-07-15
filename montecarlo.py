import pandas as pd
import numpy as np
import random

class Die:
    '''
    A die has a number of “faces” and weights, and can be rolled to select a face.
    The Die class takes an array of faces and initializes the weights to 1.0 for each face
    which can be changed. The die has one behavior, which is to be rolled one or more times.
    '''
    
    def __init__(self, faces):
        '''
       The init method initializes the die with an array of faces as an argument. 
       It initializes the weights to 1.0 for each face and saves both faces and weights 
       to a dataframe that is used for other methods in the class.
    
        PURPOSE: Given an array of faces, initializes the weights to 1.0 for each face. 
        Saves faces and weights to a dataframe.
    
        INPUTS
        faces   array of strings or numbers      
        '''
        self.faces = faces
        self.df = pd.DataFrame(columns=faces)
        self.df.loc[0] = 1.0
        
    def weights(self, face, weight):
        '''
        The weights method changes the weight of a single face. It takes a face value 
        and weight value and changes the weight of the face if it is in the array of faces. 
    
        PURPOSE: Given a face and weight, changes the weight of a single face if the face 
        is in the array and the weight is a float or int. Returns False if face is not 
        in the array.
    
        INPUTS
        face     string or number
        weight   int or float 
        '''
        if face in self.faces:
            if type(weight) == float or type(weight) == int:
                self.df.at[0,face] = weight
        else:
            return False
        
    def roll(self, rolls=1):
        '''
        The roll method rolls the die one or more times. It returns a list of outcomes 
        after taking a random sample from the vector of faces according to their weights. 
        The number of rolls defaults to 1.
    
        PURPOSE: Given the number of rolls, takes random sample from the vector of faces 
        according to their weights, and returns a list of outcomes.
    
        INPUTS
        rolls    int (number of rolls, defaults to 1)
    
        OUTPUT
        list    list of random sample of vector of faces according to their weights
        '''
        weights = self.df.values.tolist()
        return list(random.choices(self.faces, weights[0], k=rolls))
    
    def show(self):
        '''
        The show method displays the die's current set of faces and weights in a dataframe.
    
        PURPOSE: Returns the dataframe created in the initializer with the current set 
        of faces and weights.

        OUTPUT
        df  dataframe with die's current set of faces and weights
        '''
        return self.df

        
        
class Game:
    '''
    A game consists of rolling one or more dice of the same kind one or more times. 
    The Game class takes a die object from the Die class and has a behavior to play 
    a game. The class also keeps the results of its most recent play.
    '''
    
    def __init__(self, die_obj):
        '''
        The init method initializes a die object from the Die class and an empty 
        dataframe to be used in the other methods.
    
        PURPOSE: Initializes a die object from the Die class so that a game can be 
        played using the die. Creates an empty dataframe that is used in other methods.
    
        INPUTS
        die_obj   list of already instantiated similar Die objects
        '''
        self.die_obj = die_obj
        self.gamedf = pd.DataFrame()
    
    def play(self, x):
        '''
        The play method takes a parameter of how many times the dice should be rolled 
        and saves the result of the play to a dataframe. 
    
        PURPOSE: Rolls dice using the roll method from the Die class and saves results
        to dataframe.
    
        INPUTS
        x    int (number of rolls)
        
        OUTPUT
        gamedf    dataframe of results of game
        '''
        for die in self.die_obj:
            new = pd.Series(die.roll(x))
            self.gamedf = pd.concat([self.gamedf, new], axis=1)
        self.gamedf.index = ['Roll ' + str(i) for i in range(1, x+1)]
        self.gamedf.columns = ['Die ' + str(i) for i in range(1, len(self.die_obj) + 1)]
        return self.gamedf 
                             
    def show(self, form = 'wide'):
        '''
        The show method passes the dataframe to the user. It takes a parameter to 
        return the dataframe in narrow or wide form, the default form.
    
        PURPOSE: Returns a dataframe of results of game in either wide or narrow form.
    
        INPUTS
        form    str ('wide' or 'narrow')
    
        OUTPUT
        gamedf   dataframe of results either in wide or narrow form
        '''
        if form == 'wide':
            return self.gamedf
        if form == 'narrow':
            return self.gamedf.stack()
        else:
            return 'Not valid form option.'
        
       
    
class Analyzer:
    '''
    An analyzer takes the results of a single game and computes various descriptive 
    statistical properties about it, including face counts per roll, a jackpot count, and a combo count. 
    The analyzer class takes a game object from the Game class to perform the methods on.
    '''
    
    def __init__(self, game_obj):
        '''
        The init method takes a game object from the Game class as its input parameter and 
        infers the data type of the die faces used.
    
        PURPOSE: Initializes a game object from the Game class to use for other methods.
    
        INPUTS
        game_obj   game object (from the Game class)
        '''
        self.game_obj = game_obj
        self.face_dtype = type(self.game_obj.die_obj[0].faces[0])
    
    def jackpot(self):
        '''
        The jackpot method computes how many times the game resulted in all faces being identical. 
        It returns an integer for the number of jackpots and stores the results in a dataframe.
    
        PURPOSE: Returns integer for number of times the game results in all faces being identical 
        and stores results in dataframe.
    
        OUTPUT
        count   int (number of times the game resulted in all faces being identical)
        '''
        self.jackpotdf = pd.DataFrame(index=self.game_obj.gamedf.index, columns=['Jackpot'])
        lst = []
        for index,rows in self.game_obj.gamedf.iterrows():
            lst.append(set(rows))
        for i in range(len(lst)):
            if len(lst[i]) == 1:
                self.jackpotdf.iat[i,0] = True
            else:
                self.jackpotdf.iat[i,0] = False
        count = self.jackpotdf[self.jackpotdf['Jackpot'] == True].count()
        return count[0]
                
    def combo(self):
        '''
        The combo method computes the distinct combinations of faces rolled, along with their counts. 
        Combinations are sorted and and saved as a multi-columned index.
    
        PURPOSE: Returns dataframe of sorted combinations of faces rolled with their counts.
    
        OUTPUT
        data   dataframe (roll number as named index and Count column for number of combinations)
        '''
        df = self.game_obj.gamedf
        cols = list(df.columns)
        data = pd.DataFrame((df.groupby(cols).size()))
        data.columns = ['Count']
        return data
    
    def faceCountsPerRoll(self):
        '''
        The faceCountsPerRoll method computes how many times a given face is rolled in each event. 
        It stores the results as a dataframe that has an index of the roll number and face values 
        as columns.
    
        PURPOSE: Returns dataframe of how many times a given face is rolled in each event.
    
        OUTPUT
        facecount  dataframe (index of the roll number and face values as columns)
        '''
        self.facecount = pd.DataFrame(columns = self.game_obj.die_obj[0].faces)
        for i in self.game_obj.gamedf.index:
            self.facecount = self.facecount.append(self.game_obj.gamedf.T[i].value_counts())
            self.facecount = self.facecount.fillna(0)
            self.facecount = self.facecount.astype(int)
        return self.facecount