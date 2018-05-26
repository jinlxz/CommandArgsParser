import sys
def test_var_scope(var):
    var=2
if __name__=="__main__":
    a=0
    test_var_scope(a)
    print "a is {0}".format(a)