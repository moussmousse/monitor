import matplotlib.pyplot as plt
from datetime import datetime


with open ("../var/ram.1s") as f:
  lines = f.readlines()


with open("../var/ram.1m", "a") as f2:
    f2.write(lines[len(lines)-1])