#rewrites the Grading script to be a function
#score = input("Enter a score between 0.0 and 1.0:")
def computegrade(score):
    try:
        score_int = float(score)
        #print("Enter score: "+score)
    except:
        #print("Enter score: "+score)
        grade = ("Bad score")
        return grade
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
    return grade

y = input("Enter a score between 0.0 and 1.0:")
x = computegrade(y)
print ("Enter score: "+y)
print(x)

#x = computegrade(.95)
#print(x)
#x = computegrade("perfect")
#print(x)
#x = computegrade(10)
#print(x)
#x = computegrade(.75)
#print(x)
#x = computegrade(.5)
#print(x)
