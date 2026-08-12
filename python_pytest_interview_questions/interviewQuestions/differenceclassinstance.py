class Myclass:

    @classmethod
    def class_method(cls):
        return "Class Method"
    
    def instance_method(self):
        return "Instance Method"
    

obj = Myclass()
print(Myclass.class_method())  # Output: Class Method
print(obj.instance_method())  # Output: Instance Method