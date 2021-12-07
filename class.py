class person:
    # like a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Jacob", 13)
print(p1.name)
# to delete a object
del p1