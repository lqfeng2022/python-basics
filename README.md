INTRO:

This book provides a simple introduction to the Python programming language, perfect for beginners interested in Computer Science, programming, Artificial Intelligence or Machine learning.
Let’s take a look at what you’ll learn in this book:


• Data Types & Variables

Since everything in the computer is data, Python uses three basic data types to represent it: numbers, strings and booleans. We assign these data to variable, which act as references to the data stored in computer memory. 
Once we have data, we can work with it using various operators, such as +, -, *, /, +=, -=, [], [:] and so on.

![image](https://github.com/user-attachments/assets/6e9e55a1-13db-4f9d-94a8-d40706b89f32)


• Control Flow Statements

Sometimes we need to perform certain actions based on specific conditions. This is where the if statement comes in. If a conditional expression evaluates to True, the code block following the if statement will execute. 
These conditional expressions often use comparison operators (e.g., >, >=, <, <=, etc.) and logical operators (and, or, not). Together, these tools form an essential part of what we call Control Flow Statements.

![image](https://github.com/user-attachments/assets/f6138de4-bd10-4ab2-b498-6ac3543c50fb)

Another important category of Control Flow Statements is loop statements, which include for loops and while loops:
  1. For loops: Allow us to perform repetitive actions on iterables (sequences of data that can be iterated over, like lists or strings).
  2. While loops: Similar to for loops, but they keep running as long as a condition remains True. However, it’s crucial to watch out for infinite loops, which can occur if the condition never becomes False.

These control flow statements are the building blocks for writing more advanced and dynamic programs.


• Functions

![image](https://github.com/user-attachments/assets/c1000772-871b-4566-82e3-96071d3e3894)

Sometimes, you will need to repeat the same task multiple times. If we write the same code over and over again, it will be tedious and inefficient. That’s where functions come in! Functions let us group code into reusable blocks. Once you define a function, you can simple call it. This keeps your code organized and saves a ton of effort.


• Data Structures

To work with data more efficiently, it’ often helpful to organize it into slightly more complex data structures. For example:

![image](https://github.com/user-attachments/assets/e1978e41-c3b3-4b3d-a43b-214b452c8c13)

  1. Lists: Sequences of data that can be modified.
  2. Tuples: Similar to lists but immutable, meaning their content cannot be changed.
  3. Sets: Collection of unique elements, ensuring no duplicates.
  4. Dictionaries: Collections of key-value pairs, allowing you to map and retrieve data based on a key.


• Data Manipulations

With these data structures, we can handle data much more effectively. Tasks like accessing, mapping, filtering, sorting, and unpacking data become easier and more intuitive.

![image](https://github.com/user-attachments/assets/5e872d52-575d-4bf6-982e-c7f7aab6c2f6)


• Lambda function & List Comprehension

When working with iterables, we often use a for statement to iterate through them and perform operations. however, there’s a simpler way: lambda functions. With lambda functions, we can condense a for loop into a single, concise expression. 

![image](https://github.com/user-attachments/assets/33812b8d-85f4-4464-81c6-998fe3eeef87)

Even better, we have list comprehensions, which are more Pythonic and make the code cleaner and easier to read. Beyond lists, comprehensions can also be used with sets and dictionaries, make them a versatile choice for working with data.


• Exceptions

Let’s face it — no program runs perfectly every time. Errors and bugs are bound to happen. That’s why it’s crucial to handle these issues properly. By managing exceptions, we can identify and understand errors more easily.

![image](https://github.com/user-attachments/assets/8aa1fe99-57f7-438f-bbe0-43c1a3cf78ae)


If we don’t handle exceptions, our program might crash unexpectedly, leaving us stuck trying to figure out what went wrong. Handling errors effectively ensures our code runs more smoothly and is easier to debug when things go off track.


• Classes

Since Python is an object-oriented programming language, which means everything in Python is and object. But what if we want to define an abstract concept — a blue-print — that captures the common attributes and behaviors of a group of objects? That’s where classes come in, make it much easier to organize and work with related data and functionality.

For example, think of the concept of a Cat. A Cat can have common attributes like fur_color, age, and whiskers. It can also perform actions like eating, running and hunting birds — these are the methods of the Cat class.

![image](https://github.com/user-attachments/assets/a0d4e5f4-0386-40f1-99b5-520865d1e940)

Using the Cat class as a blueprint, we can create specific instances like white_cat or black_cat. By grouping related attributes and methods into a class, we can efficiently organize our code and reuse it in different parts of our program.


• Inheritances & Polymorphism 

When we want to create a new class, we can inherit from an existing class, called the parent or base class. This allows the new class to use the attributes and methods of the parent class. Pretty cool, right? 
There are different types of inheritance, such as multiple inheritance and multi-level inheritance:

![image](https://github.com/user-attachments/assets/c4d366b1-806b-4e35-a12b-e56cbb1a12b1)

  1. Multi-level inheritance: For example, a Cat class could inherit from a Mammal class, which in turn inherits from an Animal class.
  2. Multiple inheritance: A Cat class could inherit from both an Mammal class and a Pet class, combining features from both.

Another key concept is polymorphism, which allows child classes to implement the same method as the parent class, but in a way that’s unique to the child.  In Python, there are more Pythonic ways to handle polymorphism (the Duck Typing principle), and you can dive deeper into them as you progress.

![image](https://github.com/user-attachments/assets/781494a7-b9c5-4b22-9ee3-f87243232294)


• Modules & Packages 

Until now, everything we’ve discussed involves writing code in a single file. In Python, a single file of code is called a module.  But as our program grows, putting all the code into one module can quickly become messy and it’s hard for reading and management. A better approach is to organize related code into separate modules.

We can take this a step further by arranging these modules into directories or folders, which Python refers to as packages. This works just like the file management system on your computer, making it easier to organize and structure your program.

![image](https://github.com/user-attachments/assets/196c2641-a902-487c-b452-9e6d7fd0b251)


• Python Standard Library

So far, the functions, classes, and exceptions we’ve used are all part of Python’s Standard Library, which forms the foundation of the Python programming language.

![image](https://github.com/user-attachments/assets/7b505c52-4942-416f-850a-30b3fb314b5a)

The Standard Library makes it easy to handle tasks like managing module and package paths. But its capabilities go far beyond that. It also lets us work with various file types, such as ZIP files, JSON files, database files, and more, making it a powerful toolset for a wide range of programming tasks.


• Python Package Index (PyPI)

Python is powerful—but why? What makes it so versatile? If we only relied on the Python Standard Libraries, it wouldn’t be enough. The real power of Python comes from the Python Package Index (PyPI). PyPI is an extensive repository of packages, and if you visit pypi.org, you’ll find over 600,000 projects currently registered there.

![image](https://github.com/user-attachments/assets/b104fa82-606e-4909-b867-7200cc241c5a)

To use these packages effectively, there’s a handy tool called pipenv. Similar to npm in JavaScript, pipenv helps manage packages from PyPI by allowing us to install, uninstall, update, and more.

![image](https://github.com/user-attachments/assets/c303f8e8-6d14-4b50-9540-89a7e62cfe5d)

Unlike the built-in pip tool, pipenv lets us create isolated virtual environments that contain all the dependencies for each specific project. This way, we can manage projects separately, avoiding the mess and complexity of sharing global packages across multiple projects.


• What’s Next

By the time you finish this book, you’ll have a solid understanding of the basics of Python. From here, you can start building your own projects, like a web crawler, a Django project, or even a deep learning model with PyTorch or TensorFlow. These are the next steps in your Python journey — and we’ll dive into these topics soon!

![image](https://github.com/user-attachments/assets/8a2067ba-f3d1-4706-825f-a7116caff60b)

