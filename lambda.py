def func(a, b, operation):
    print (operation(a, b))


func(2, 10, lambda a, b : a + b)   
func(2, 10, lambda a, b : a * b)
