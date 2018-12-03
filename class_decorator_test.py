class Foo(object):
    def __init__(self, funk):
        self._func = funk

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()