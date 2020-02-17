#!/usr/bin/env python

import unittest
import nbconvert
import os

import numpy as np

with open("assignment8.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment8.py", "w") as f:
    f.write(python_file)


from assignment8 import Toughness

class TestSolution(unittest.TestCase):

    def test_toughness(self):

        ss = Toughness('data.dat')

        np.testing.assert_allclose(ss.compute_toughness_simps(), 70836.23, atol=0.01)
        np.testing.assert_allclose(ss.compute_toughness_trapz(), 70836.14, atol=0.01)

    def test_toughness_private(self):

        ss = Toughness('data_private.dat')

        np.testing.assert_allclose(ss.compute_toughness_simps(), 42744.49, atol=0.01)
        np.testing.assert_allclose(ss.compute_toughness_trapz(), 42744.44, atol=0.01)
        
if __name__ == '__main__':
    unittest.main()

