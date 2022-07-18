# # Assigning function to a variable

# def funct():
#     print('This function was called through a variable.')

# new_var = funct

# new_var()


# ----------------------------------------------------------------------------------------------------


# # function within a function

# def outer_funct():
#     print('Outer function.')

#     def inner_funct():
#         print('Inner function returned.')

#     return inner_funct()

# outer_funct()

# ------------- OR ---------------

# # function within a function called inside

# def outer_funct():
#     print('Outer function.')

#     def inner_funct():
#         print('Inner function returned.')

#     inner_funct()

# outer_funct()

# ------------- OR ---------------

# # function within a function called outside with ERROR

# def outer_funct():
#     print('Outer function.')

#     def inner_funct():
#         print('Inner function returned.')

# inner_funct()


# ---------------------------------------------------------------------------------------------------


# function within a function called by a variable

# def outer_funct():
#     print('Outer function.')

#     def inner_funct():
#         print('Inner function returned.')

#     return inner_funct()

# run_func = outer_funct

# run_func()

# # ------------- OR ---------------

# run_func = outer_funct()

# run_func


# ---------------------------------------------------------------------------------------------------


# function passed as an arguement

# def answer(funct):
#     funct()
#     print('Answer : Mount Everest.')

# def question():
#     print("Question : Name the tallest peak in the world.")

# answer(question)

# # ------------- OR ---------------

# KBC = answer
# KBC(question)

# # ------------- OR ---------------

# KBC = answer(question)
# KBC


# ---------------------------------------------------------------------------------------------------


# PYTHON DECORATOR

# def Amitabh_Bachchan(funct):

#     def Agla_prashnn():
#         print("Agla Prashnn! Yeh rha aapki computer screen par!")
#         funct()
#         print("A. Yeshwant Sinha            B. Venkya Naidu")
#         print("C. Draupadi Murmu            D. Murli Manohar Joshi")
#     return Agla_prashnn()

# @Amitabh_Bachchan
# def KBC_3L20K():
#     print("Name the current NDA candidate for the Indian Presidential Election 2022.")

# KBC = Amitabh_Bachchan
# KBC


# ---------------------------------------------------------------------------------------------------


# def Doc_Oc(funct):
#     name = str(input("Enter the name : "))
#     def wrapper(*args, **kwargs):
#         print('Doctor Octopus emerges from within the crumbling highway road.')
#         funct(name)
#         print(f'{name} looks confused & turns into Iron-Spider.')
#     return wrapper(name)
# @Doc_Oc
# def dialogue(name):
#     print(f'Hello {name}...')

# Doc_Oc


# ---------------------------------------------------------------------------------------------------


# CHAINING DECORATORS WITH PARAMETERS

# def decor1(funct):
#     def wrapper1(*args):
#         print("%"*30)
#         funct(*args)
#         print("%"* 30)
#     return wrapper1

# def decor2(funct):
#     def wrapper2(*args):
#         print("*"*30)
#         funct(*args)
#         print("*"* 30)
#     return wrapper2

# @decor2
# @decor1
# def printer(msg):
#     print(msg)

# printer('Hello!')


# # ------------- OR ---------------


# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner


# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner


# @star
# @percent
# def printer(msg):
#     print(msg)


# printer("Hello")


# ---------------------------------------------------------------------------------------------------



