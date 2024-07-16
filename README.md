
# In Python, 
Classes are blueprints for creating objects. They define the properties (attributes) and behaviors (methods) that objects of that class will share. Here's a breakdown of classes and how to use them with an example:

- Concepts:

Class: A blueprint that defines the structure of objects. It specifies the attributes (variables) that objects will have and the methods (functions) that objects can perform.
Object: An instance of a class. It represents a specific entity with its own set of attributes and methods defined by the class.

- Benefits of Classes:

Code Reusability: Classes allow you to define the structure and behavior of objects once and then create multiple objects (instances) with the same characteristics, reducing code duplication.
Data Encapsulation: You can control access to object attributes and methods by defining them as private, public, or protected within the class.
Object-Oriented Programming: Classes are fundamental building blocks of object-oriented programming (OOP), a powerful paradigm for structuring complex applications.


# Methods

1. Instance Methods:

Definition: Instance methods are the most common type of methods in Python classes. They are defined within the class and operate on specific instances (objects) of the class.
Access: Instance methods are accessed using dot notation (object_name.method_name(arguments)) on an object.
self Argument: Instance methods implicitly take a first argument self which refers to the current object instance. This allows them to access and modify the object's attributes within the method.

2. Class Methods:

Definition: Class methods are methods that are bound to the class itself, not to specific objects (instances). They are typically used for operations that are related to the class as a whole rather than individual objects.
Access: Class methods are accessed using the class name followed by dot notation (ClassName.method_name(arguments)) and do not require creating an object instance first.
cls Argument: Class methods take a first argument cls which refers to the class itself (similar to self for instance methods).

3. Static Methods:

Definition: Static methods are not bound to the class or its objects. They are essentially regular functions that are defined within the class namespace for utility purposes. They don't have implicit access to self or cls arguments.
Access: Static methods are accessed using the class name followed by dot notation (ClassName.method_name(arguments)), similar to class methods.
No Special Arguments: Static methods don't take self or cls arguments by default.

#### Choosing the Right Method Type:

Use instance methods for actions that operate on specific object data (attributes).
Use class methods for operations related to the class itself, often used as alternative constructors or factory methods.
Use static methods for utility functions that don't require access to class data or don't modify class state directly.



### Docker

- Dockerfile -: restapi/Dockerfile
- Docker Compose file -: restapi/docker-compose.yml

### Commands
1. flask run
2.  docker build -t python-rest-apis .
3.  docker compose up