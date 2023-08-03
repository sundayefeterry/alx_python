#!/usr/bin/python3
"""
This is an empty BaseGeometry class.
"""


class BaseGeometry:
    ''' 
    Class: BaseGeometry
    '''
    def __dir__(self):
        attributes = super().__dir__()
        return [attr for attr in attributes if attr != '__init_subclass__']
    pass
