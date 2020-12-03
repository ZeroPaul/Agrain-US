#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def percent_all(total, list_master):
    result = {}
    for k in list_master.keys():
        percent = (int(list_master[k])/total) * 100
        result[k] = percent
    return(result)


# d = {'cce9412e-7813-416d-aaff-515aee306c4e': 2, 
#     '1ca4ae28-efab-47cc-a6e7-ae62491bd02b': 2}

# percent_all(4, d)
