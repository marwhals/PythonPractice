import pandas as pd
import os
from quandl import quandl
import time

auth_tok = "r_E47v_s_LShwprQbLGh"

data = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken=auth_tok)

print(data)
