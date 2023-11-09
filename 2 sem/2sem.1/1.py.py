from abc import ABC, abstractmethod

class Box(ABC):
  
  @abstractmethod
  def add(self):
    pass
    
  def empty(self):
    pass
    
  def count(self):
    pass


class Item:

  def __init__(self, name, value):
    self.name=name
    self.value=value

class ListBox(Box):

  def __init__(self):
    self.box_list=[]
  
  def add(self, other):
    self.box_list.append(other)
    
  def empty(self):
    extraction=self.box_list
    self.box_list=[]
    return extraction
    
  def count(self):
    return len(self.box_list)


class DictBox(Box):

  def __init__(self):
    self.box_dict={}
  
  def add(self, other):
    self.box_dict[(other, other.value)]=other
    
  def empty(self):
    extraction=list(self.box_dict.values())
    self.box_dict={}
    return extraction
    
  def count(self):
    return len(self.box_dict)


def repack_boxes(*boxes):
  general_box=[]
  for box in boxes:
    empty_box=box.empty()
    for thing in empty_box:
      general_box.append(thing)
  sum_thing, sum_boxes=len(general_box), len(boxes)
  rest=sum_thing%sum_boxes
  for _ in range(sum_thing//sum_boxes):
    for box in boxes:
      box.add(general_box[0])
      del general_box[0]
  boxes=list(boxes)
  if rest!=0:
    for num in range(rest):
      boxes[num].add(general_box[0])
      del general_box[0]
    
listbox_1=ListBox()
listbox_2=ListBox()
dictbox_1=DictBox()

for element in range(20):
  listbox_1.add(Item(str(element), element))

for element in range(9):
  listbox_2.add(Item(str(element), element))

for element in range(5):
  dictbox_1.add(Item(str(element), element))

print(f"listbox_1: {listbox_1.count()}, listbox_2: {listbox_2.count()}, dictbox_1: {dictbox_1.count()}")

repack_boxes(listbox_1, listbox_2, dictbox_1)

print(f"listbox_1: {listbox_1.count()}, listbox_2: {listbox_2.count()}, dictbox_1: {dictbox_1.count()}")
