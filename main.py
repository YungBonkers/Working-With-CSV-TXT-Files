
student_scores = {
    "Jared": ([97, 85, 45], []),
    "John": ([90, 70, 65,], []), 
    "James": ([90, 100, 87], []), 
    "Joe": ([90, 84, 75], []), 
    "Jackson": ([90, 55, 67], []),
}

for name, (score, avgscore) in student_scores.items():
    avg_score = round(sum(score) / len(score), 2)
    avgscore.append(f"avg score: {avg_score}")

with open("student_scores.csv", "w+") as csv_file:
    for name, score in student_scores.items():
        csv_file.write(f"{name}, {score}\n")
        
with open("student_scores.csv", "r") as csv_file:
    content = csv_file.readlines()
      
with open("avg_scores.txt", "w+") as text_file:
    
    for row in content:
        text_file.write(row)

text_file_path = "avg_scores.txt"

with open(text_file_path, "r") as text_file:
    content = text_file.read()

print(content)

    