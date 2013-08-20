#!/usr/bin/python

import sys

testlist = ['paint', 'patch', 'sand', 'pick colors']

def compare(a, b):
    print('Which comes first: %s or %s?') % (a, b)
    ret = raw_input('> ')
    if ret not in [a,b]:
        print 'Please choose from the options provided'
        ret = compare(a,b)
    return ret

def prioritize_list(l):
    if len(l) <= 1: return l
    pivot = l[len(l)/2]
    l.remove(pivot)
    before = []
    after = []
    for i in l:
        winner = compare(i, pivot)
        if winner == pivot:
            after += [i] 
        else:
            before += [i]
    print before, after 
    return prioritize_list(before) + [pivot] + prioritize_list(after)

if __name__=="__main__":
    ordered_list = prioritize_list(sys.argv[1:])
    print ordered_list
