# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:07:44 2022

@author: Joao
"""

import pandas as pd
import numpy as np 
import sys
from matplotlib import pyplot as plt

coviddata = pd.read_excel("Covid19Data-US.xlsx")

from pandas_profiling import ProfileReport
prof = ProfileReport(coviddata)
prof.to_file(output_file='coviddata.html')
