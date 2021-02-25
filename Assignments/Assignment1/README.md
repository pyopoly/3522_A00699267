# COMP3522_Assignment1_A00699267_A01172507

BCIT Winter 2020/2021\
Comp 3522\
author: Tegvaran Sooch & Jack Shih

--------------------------------------
Assignment 1: The F.A.M.
(Family Appointed Moderator)\
The FAM program represents a parental control management program on their child's spending.
The parent can register a child and assign budgets to the child. If the child overspends, the budget is locked.

--------------------------------------

fam.py
--------------------------------------
class: FAM\
Main class of this Program.

ui.py
--------------------------------------
class: UI\
Front-end class. Prints out information for the user.

bank_account.py
--------------------------------------
classes: BankAccount, Transaction, Budget, and Enum Category.\
Contains banking information for the user, including their transactions, their budgets, and their bank balance.

user.py
--------------------------------------
classes: User, Child, Angel, TroubleMaker, and Rebel.\
Contains classes that represent the User for this program. User and Child classes are not supposed to be instantiated.