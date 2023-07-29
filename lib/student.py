#!/usr/bin/env python

from user import User
from teacher import Teacher

class Student(User):
    
    def __init__(self, first_name, last_name):
        User.__init__(self, first_name, last_name)
        self.knowledge = []
             
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)
    