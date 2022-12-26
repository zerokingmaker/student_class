class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) == Grade :
      self.grades.append(grade.score)

  def get_average(self):
    if len(self.grades) == 0 :
      print("You have no grades")
    else :
      average = sum(self.grades) / len(self.grades)
      print(average)
    
  attendance = {"Monday" : 0, "Friday" : 0}


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self):
    if self.score >= self.minimum_passing :
      print("Pass")
    else : 
      print("Fail")


new_grade = Grade(100)
new_grade.is_passing()
pieter.add_grade(new_grade)
pieter.add_grade(new_grade)
print(pieter.attendance)
pieter.get_average()
