import random

class Multiply:
  def __init__(self):
    self.mutate()

  def mutate(self):
    self.k = random.randint(-100, 100)

  def exec(self, n1, n2):
    return ( n1 * n2 ) + self.k
