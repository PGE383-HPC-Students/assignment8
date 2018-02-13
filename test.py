#!/usr/bin/env python

from assignment8 import Toughness

import numpy as np

def test_toughness_1():
    
    ss = Toughness('data_1.dat')
    
    np.testing.assert_allclose(ss.compute_toughness_simps(), 70836.23, atol=0.01)
    np.testing.assert_allclose(ss.compute_toughness_trapz(), 70836.14, atol=0.01)
    
def test_toughness_2():
    
    ss = Toughness('data_2.dat')
    
    np.testing.assert_allclose(ss.compute_toughness_simps(), 42744.49, atol=0.01)
    np.testing.assert_allclose(ss.compute_toughness_trapz(), 42744.44, atol=0.01)

