# 1. SINGLE INHERITANCE

# class Parent:
#     print('Parent of child.')

# class Child(Parent):
#     print("Child.")

# child = Child()
# child


# -----------------------------------------------------------------------


# 2. MULTIPLE INHERITANCE

# class Grandparent:
#     def gp_intro(self):
#         print("Grandparent of child.")

# class Parent:
#     def p_intro(self):
#         print('Parent of child.')

# class Child(Parent, Grandparent):
#     def c_intro(self):
#         print("Child.")

# child = Child()
# child.gp_intro()
# child.p_intro()
# child.c_intro()


# -----------------------------------------------------------------------


# 3. MULTI-LEVEL INHERITANCE

# class Grandparent:
#     def gp_intro(self):
#         print("Grandparent of child.")

# class Parent(Grandparent):
#     def p_intro(self):
#         Grandparent.gp_intro(self)
#         print('Parent of child.')

# class Child(Parent):
#     def c_intro(self):
#         Parent.p_intro(self)
#         print("Child.")

# child = Child()
# child.c_intro()


# -----------------------------------------------------------------------


# 4. HIERARCHICAL INHERITANCE

# class Grandparent:
#     def gp_intro(self):
#         print("Grandparent of children.")

# class Parent(Grandparent):
#     def p_intro(self):
#         Grandparent.gp_intro(self)
#         print('Parent of child.')

# class Child(Grandparent):
#     def c_intro(self):
#         Grandparent.gp_intro(self)
#         print("Child.")

# class Child_2(Grandparent):
#     def c_2_intro(self):
#         Grandparent.gp_intro(self)
#         print("Child 2.")

# parent = Parent()
# parent.p_intro()

# child = Child()
# child.c_intro()

# child_2 = Child_2()
# child_2.c_2_intro()


# -----------------------------------------------------------------------


# 5. HYBRID INHERITANCE

# class Grandparent_1:
#     def gp_intro_1(self):
#         print("Grandparent of children.")

# class Parent_1(Grandparent_1):
#     def p_intro_1(self):
#         Grandparent_1.gp_intro_1(self)
#         print('Parent of child.')

# class Grandparent_2:
#     def gp_intro_2(self):
#         print("Grandparent of children.")

# class Parent_2(Grandparent_2):
#     def p_intro_2(self):
#         Grandparent_2.gp_intro_2(self)
#         print('Parent of child.')

# class Child(Parent_1, Parent_2):
#     def c_intro(self):
#         print("Child.")

# child = Child()
# child.c_intro()
# child.p_intro_1()
# child.p_intro_2()


# -----------------------------------------------------------------------


