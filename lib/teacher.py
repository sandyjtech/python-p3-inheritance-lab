#!/usr/bin/env python
#import ipdb
from user import User 
import random

class Teacher(User):   
 
    def __init__(self, first_name, last_name):
        User.__init__(self, first_name, last_name)
        
        
    def teach(self):
        return random.choice(self.knowledge)
        
#ipdb.set_trace()