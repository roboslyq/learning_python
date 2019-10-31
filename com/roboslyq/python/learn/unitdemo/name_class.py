class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_all(self):
        print("id:" + self.id)
        print("name:" + self.name)
        return self.id + ":" + self.name

    def print_id(self):
        print("id:" + self.id)
        return self.id

    def print_name(self):
        print("name:" + self.name)
        return self.name
