# 0x0C. Python - Almost a circle

## Tasks

### 0. If it's not tested it doesn't work
All your files, classes and methods must be unit tested and be PEP 8 validated.
* File: tests/

### 1. Base class
Write the first class Base
* File: models/base.py, models/__init__.py

### 2. First Rectangle
Write the class Rectangle that inherits from Base
* File: models/rectangle.py

### 3. Validate attributes
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
* File: models/rectangle.py

### 4. Area first
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
* File: models/rectangle.py

### 5. Display #0
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
* File: models/rectangle.py

### 6. __str__
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
* File: models/rectangle.py

### 7. Display #1
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
* File: models/rectangle.py

### 8. Update #0
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
* File: models/rectangle.py