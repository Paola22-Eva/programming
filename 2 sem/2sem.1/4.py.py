
class Learner:
  def __init__(self):
      self.classes = []

  def enrol(self, course):
      self.classes.append(course)
    
class Teacher:
  def __init__(self):
      self.courses_taught = []

  def assign_teaching(self, course):
      self.courses_taught.append(course)

class Person:
  def __init__(self, name, surname, number, learner=None, teacher=None):
      self.name = name
      self.surname = surname
      self.number = number

      self.learner = learner
      self.teacher = teacher

  def enrol(self, a_postgrad_course):
    assert (self.learner is not None), "атрибут learner не установлен"
    self.learner.enrol(a_postgrad_course)

  def assign_teaching(self, an_undergrad_course):
    assert (self.teacher is not None), "атрибут teacher не установлен"
    self.teacher.assign_teaching(an_undergrad_course)
  

jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
a_postgrad_course, an_undergrad_course="a_postgrad_course", "an_undergrad_course"
jane.enrol(a_postgrad_course)
jane.assign_teaching(an_undergrad_course)