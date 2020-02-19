score = input("Enter a score between 0.0 and 1.0:")
try:
    score_int = float(score)
except:
    print("Bad score")
    quit()
if score_int<0 or score_int>1.0:
    grade=("Bad score")
elif score_int>=0.9:
    grade="A"
elif score_int>=0.8:
    grade="B"
elif score_int>=0.7:
    grade="C"
elif score_int>=0.6:
    grade="D"
else:
    grade="F"
print(grade)
