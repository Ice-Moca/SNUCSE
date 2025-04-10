def test_func_num( passed_data ):
    print("Address of passed data  is ", id(passed_data))
    passed_data = passed_data + 10
    print("Address of newly created passed_data  is ", id(passed_data))
    
def my_func_num():
    my_data = 10
    print("Address of my_data  is ", id(my_data))
    test_func_num(my_data)
    print("After calling test_func_num( ): the value of my_data ==> ", my_data )
    print("Address of my_data  after function-call is ", id(my_data))

my_func_num()

