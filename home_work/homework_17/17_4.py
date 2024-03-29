#!/usr/bin/python3

class String(str):

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return String(str(self.value) + str(other))

    def __sub__(self, other):
        return String(str(self.value).replace(str(other), '', 1))

