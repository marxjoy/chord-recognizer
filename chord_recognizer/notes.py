import random

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#']
#types = ['', 'm' , 'dim', 'aug']
types = {'major': '',
         'minor': 'm' ,
         'dimnished': 'dim', 
         'augmented': 'aug' }




def random_root():
    return random.choice(notes)

def random_type():
    return random.choice(list(types.values()))