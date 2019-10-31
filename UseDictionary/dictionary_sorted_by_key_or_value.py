# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:07:50 2019
Sort dictionary by key or value

@author: dina
"""

from collections import OrderedDict

def make_dictionary():
    """
    make and return dictionary
    key = fruit name
    value = price float number
    """
    items = {"banana": 11.34, "apple": 15.55, "orange": 15.55, "limon": 3.20,
             "apple pink": 16.60}
    return items


def sort_by_key(d):
    """
    get dictionary of type  name:float number 
              can be empty dictionary
    return dictionary sorted by key(name)
    """
  
    try:        
        d = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    except:
        d = {}
    return d


def sort_by_value(d):
    """
    get dictionary of type  name:float number 
              can be empty dictionary
    return dictionary sorted by value(price)
    """
 
    try:        
        d = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    except:
        d = {}
    return d

        
def main():
    dic = make_dictionary()
    print("\ndictionary by input", dic)
    
    dic_by_key = sort_by_key(dic)    
    #print("\n\ndictionary sorted by key", dic_by_key)
    print("\n\ndictionary sorted by key")
    for k, v in dic_by_key.items():
        print (k, v)
    
    dic_by_value = sort_by_value(dic)
    print("\ndictionary sorted by value", dic_by_value)


if __name__ == '__main__':
    main()