# desing-patterns-python

## This course will teach you how to use proven object-oriented design patterns to significantly enhance the stability, testability, and maintainability of your Python development while decreasing your development time.

## Design Pattern

A desing pattern is a model solution to a common design problem.
It describes the problem and a general approach to solving it.

We need design patterns to ensure that our work is consisten reliable and understable

### Design Pattern Classification

-- Creational -> Object creation
-- Structural --> Object composition
-- Behavioral -> Object interaction

### Solid

-- Single responsability
-- Open/Closed
-- Liskov substitution
-- Interface segregation
-- Dependency inversion

## Interfaces in Python

### Abstract Base Class Definition

```
import abc

class MyABC(abc.ABC):
""" Abstract Base Class Definition """
    @abc.abstractmethod
    def do_something(self, value):
        """ Required method """

    @abc.abstractproperty
    def some_property(self):
        """ Required property """

```

### Concrete Class Implementation

```
class MyClas(MyABC):
""" Implementatiomn of abstract base class """
    def __init__(self, value=None):
    self.__myprop = value

    def do_something(self, value):
    self.__myprop = value

    @property
    def some_property(self):
    return self.__myprop

```
