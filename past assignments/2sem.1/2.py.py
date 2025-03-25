
from dataclasses import dataclass

@dataclass
class User_data:
  name: str
  mail_address: str
  age: int

class Exceptionuniquename(Exception):
  pass
  
class Exceptionintage(Exception):
  pass

class Exceptionless16(Exception):
  pass

class Exceptionmail(Exception):
  pass

def creating_a_directory(data_list):
  unique_name, catalog=[], []
  for data in range(len(data_list)):
    try:
      if data_list[data].name in unique_name:
        raise Exceptionuniquename()
      unique_name.append(data_list[data].name)
      
      try:
        if type(data_list[data].age)!=int or data_list[data].age<0:
          raise Exceptionintage()
        if data_list[data].age<16:
          raise Exceptionless16()
        if data_list[data].mail_address.count("@")!=1:
          raise Exceptionmail()
        if data_list[data].mail_address[0]=="@":
          raise Exceptionmail()
        if data_list[data].mail_address[-1]=="@":
          raise Exceptionmail()
        catalog.append((data_list[data].name, data_list[data].mail_address))
          
      except Exceptionintage:
        print("возраст не является положительным целым числом")
      except Exceptionless16:
        print("пользователю меньше 16 лет")
      except Exceptionmail:
        print("адрес электронной почты недействителен")
    except Exceptionuniquename:
      print("имя пользователя не уникально")
  return catalog

data_list=[User_data("Roman", "roman@mail.ru", 16), User_data("Roman", "romanchik@mail.ru", 20), User_data("Ivy", "ivy@mail.ru", 40), User_data("Lissa", "lissa@mail.ru", 20), User_data("June", "@@mail.ru", 29), User_data("Criss", "criss@", 20), User_data("Karen", "@mail.ru", 88)]
print(creating_a_directory(data_list))
  