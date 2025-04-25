class MyClass:
    # 类属性
    class_variable = "This is a class variable"

    def __init__(self):
        # 实例方法中访问类属性
        print(f"Accessing class variable using self.__class__: {self.class_variable}")

    def call_class_method(self):
        # 实例方法中调用类方法
        self.__class__.class_method()

    @classmethod
    def class_method(cls):
        print("This is a class method.")

# 创建类的实例
obj = MyClass()
# 调用实例方法来调用类方法
obj.call_class_method()