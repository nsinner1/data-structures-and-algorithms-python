class Animal:

  def __init__(self, animal_name):
    self.value = animal_name
    self.next = None


class Cat(Pet):
  type = 'dog'


class Dog(Pet):
  type = 'cat'


class AnimalShelter:

  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()

  def enqueue(self, pet):
    if isinstance(pet, Dog) or isinstance(pet, Cat):
      self.q1.enqueue(pet)
    else:
      return "Pet has to be dog or cat"
      
  def dequeue(self, pref):
        adopted_pet = None
        while not self.q1.is_empty():
            if self.q1.front.type == pref.lower() and adopted_pet == None:
                adopted_pet= self.queue1.dequeue()
            else:
                self.q2.enqueue(self.q1.dequeue())
        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())
        return adopted_pet