# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:47:06 2016

@author: leilu
"""

from scipy import spatial

def Cosine_similarity(v1,v2):
    return 1-spatial.distance.cosine(v1, v2)