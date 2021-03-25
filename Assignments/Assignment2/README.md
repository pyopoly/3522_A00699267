# COMP3522_Assignment2_A00699267_A01172507

BCIT Winter 2020/2021 \
March 2021\
Comp 3522\
author: Tegvaran Sooch & Jack Shih

--------------------------------------
Assignment 2: The Supply Chain\
For this assignment we will be simulating a store that keeps festive seasonal items all year long. That is, it keeps a stock of toys, stuffed animals, and candy that vary by holidays (Easter, Christmas and Halloween). So if you ever wanted easter eggs in december, this would be the place to go!
Your code will be taking in bulk orders that come in from the store's website in the form of excel files. The system should implement the abstract factory pattern to achieve this

--------------------------------------

store.py
--------------------------------------
class: Store, Inventory, InventoryManager, ReportManager
Store is the main class of this Program. It communicates with UI, ReportManager, InventoryManager, OrderProcessor, Order, and Factory


ui.py
--------------------------------------
class: UI<abstract>, ConsoleUI\
Front-end class. Prints out information for the user.

order.py
--------------------------------------
classes: OrderProcessor, Order.\
OrderProcessor processes orders, and also contains the factory_mapping dictionary that maps the correct factory the an Order.
Order is a data class.

factory.py
--------------------------------------
classes: AbstractFactory, Factory, ChristmasFactory, HalloweenFactory, and EasterFactory.\
Each Factory can create three types of Products: Toy, StuffedAnimal, and Candy.

products.py
--------------------------------------
classes: Product, Toy(Product), StuffAnimal(Product), Candy(Product), SantasWorkshop(Toy), RCSpider(Toy), RobotBunny(Toy), 
StuffedAnimal(Product), DancingSkeleton(StuffedAnimal), Reindeer(StuffedAnimal), EasterBunny(StuffedAnimal),
PumpkinCaramelToffee(Candy), CandyCane(Candy), CremeEgg(Candy) /
/
Exception: InvalidDataError(Exception)

contains all Products

file_handler.py
--------------------------------------
classes: FileHandler, ReadableFileSource(abc.ABC), WritableFileSource(abc.ABC), ExcelFileSource(ReadableFileSource), TxtFileSource(WritableFileSource)