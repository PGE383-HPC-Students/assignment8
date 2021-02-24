#/usr/bin/env python
#
# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

if __name__ == '__main__':
    unittest.main()

