
import abc

class AbstractFactory(metaclass=abc.ABCMeta):
  """
  Interface for operate abstract proudcts
  """
  @abc.abstractmethod
  def create_product(self):
    pass

  def name(self, factory):
    return "Fábrica " + str(factory) 

class ConcreteFactory1(AbstractFactory):

  def create_product(self):
    return ConcreteProduct1(self.name(1));

class ConcreteFactory2(AbstractFactory):

  def create_product(self):
    return ConcreteProduct2(self.name(2))



class AbstractProduct(metaclass=abc.ABCMeta):

    def __init__(self, factory):
      self.factory = str(factory);

    @abc.abstractmethod
    def create(self):
      pass

    def name(self, name):
      return self.factory + " | Product " + str(name);


class ConcreteProduct1(AbstractProduct):

    def create(self):
      return self.name("1")


class ConcreteProduct2(AbstractProduct):
  
    def create(self):
      return self.name("2")