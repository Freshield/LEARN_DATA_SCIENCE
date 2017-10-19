class Person:
    department = 'School of Information'

    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

store1 = [10,11,12,2]
store2 = [9,12,12,1]

cheapest = map(min,store1,store2)

for k in cheapest:
    print(k)