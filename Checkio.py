def checkio(anything):
    value = anything

    class MyClass(object):  
        def __str__(self):
            return ("This is testing for magic in functions")
    

print(str(checkio))
