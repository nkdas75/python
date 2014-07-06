#Python Closure
def foo(y):
    def bar(x):
        return (x+y)
    return bar
    
print (foo(1)(2))


#Python Lambda
foo = lambda y : (lambda x : x + y)

print (foo(2)(3))
