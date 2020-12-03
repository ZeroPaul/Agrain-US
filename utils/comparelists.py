#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

def list_counter(list_simple):
    result = {}
    counter=collections.Counter(list_simple)
    for k in counter.keys():
        result[k] = counter[k]
    return(result)



