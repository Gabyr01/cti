# The hour hand of an analog clock turned α degrees since the midnight.
# Determine and print the angle by which the minute hand turned since
# the start of the current hour. Input and output in this problems are integers.

# Understand:
# Match:
# Plan:
# Implementation:
# Review:
# Evaluate #Time: 
import math

hourDegree=input("Insert hour in degrees =")
#360/12 = 30 --> every hour has 30 degrees
rule=int(hourDegree)%30*12
print("The result = ",rule)