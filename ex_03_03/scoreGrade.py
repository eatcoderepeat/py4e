score = input("Enter Score: ")
score = float(score)

if score > 1.0 or score < 0 :
    print("Please enter a score between 0.0 and 1.0")

if score >= 0.9 :
    grade = "A"
elif score >= 0.8 :
    grade = "B"
elif score >= 0.7 :
    grade = "C"
elif score >= 0.6 :
    grade = "D"
elif score < 0.6 :
    grade = "F"

print(grade)
