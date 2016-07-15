class TestClassMethod(object):

    METHOD = "method hoho"

    def __init__(self):
        self.name = "leon"

    def test1(self):
        print ("test1")
        print (self.name)

    @classmethod
    def test2(cls):
        print ("test2")
        print (cls)
        
        print (TestClassMethod.METHOD)
        print ('----------------')

    @staticmethod
    def test3():
        print ("test3")
        print (TestClassMethod.METHOD)
        print ('----------------')


if __name__ == '__main__':
    a = TestClassMethod()
    a.test1()
    a.test2()
    a.test3()
    TestClassMethod().test3()