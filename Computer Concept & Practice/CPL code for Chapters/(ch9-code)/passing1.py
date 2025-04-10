def test_func_list( data ):
    data.append(20)
    
def my_func_list():
    my_list = [ 10, 5, 0 ]
    test_func_list(my_list)
    print("After calling test_func_list( ): the value of my_list ==> ", my_list )

my_func_list()
