"""Python里的instance method, classmethod与staticmethod
https://blog.csdn.net/weixin_35653315/article/details/78165645
"""
class Foo():
    # 无修饰
    def instance_method(self): #传入的第一个参数是self, 即instance本身
        print('the first argument of instance_method:', self)

    @classmethod
    def class_method(cls): # 传入的第一个参数是class
        print('the first argument of class_method:', cls)

    @staticmethod
    def static_method(): # 没有默认的首位参数, 只有自定义参数
        print('the first argument of static_method:')

foo = Foo()
foo.instance_method()
Foo.class_method()
foo.class_method()
Foo.static_method()
foo.static_method()
try:
    Foo.instance_method()
except:
    print('instance method can not be accessed through class.')