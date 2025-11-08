class copy_class:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject #list mutable objects

    @property
    def add_subjects(self):
        return self.subject

    @add_subjects.setter
    def add_subjects(self,update_subject):
        self.subject.append(update_subject)   

    def shallow_copy(self):
        new_intance= copy_class(self.name,self.subject)
        return new_intance
    
    def deep_copy(self):
        new_subject=self.subject[:]
        new_instance= copy_class(self.name,new_subject)
        return new_instance
    
    def show(self):
        print(f"My name is {self.name} & subjects{self.subject}")
        print(f"{id(self)}<....to subjects....> {id(self.subject)} ")

s1=copy_class("Ali",["math","eng","urdu"])
print("Original")
s1.show()

s1.add_subjects="sst"
s1.show()


# Corrected shallow_copy: Creates a new object whose mutable attributes
# reference the *same* mutable objects as the original.
Shallow_copy=s1.shallow_copy()
print("Shallow copy")
Shallow_copy.show()

s2=copy_class("Mubeen",["urdu","math"])
print("Original")

s2.show()
Deep=s2.deep_copy()

s2.add_subjects="science"

s2.show()

print("Depp copy")
Deep.show()


# class copy_class:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject  # list mutable objects

#     @property
#     def subjects(self):
#         return self.subject

#     @subjects.setter
#     def subjects(self, update_subject):
#         self.subject.append(update_subject)

#     
#     def shallow_copy_object(self):
#         # Create a new instance with the same name and subject list reference
#         new_instance = copy_class(self.name, self.subject)
#         return new_instance

#     # Corrected deep_copy: Creates a new object, and recursively copies
#     # all its mutable attributes (like the list 'subject').
#     def deep_copy_object(self):
#         # Create a new instance with the same name, but a *new copy* of the subject list.
#         new_subject_list = self.subject[:]  # List slicing creates a shallow copy of the list
#         new_instance = copy_class(self.name, new_subject_list)
#         return new_instance

#     def show(self):
#         print(f"My name is {self.name} & subjects: {self.subject}")
#         # Also show the object ID and subject list ID for clarity
#         print(f"Object ID: {id(self)}, Subject List ID: {id(self.subject)}")

# # --- Demonstration ---

# # 1. Initialize original object s1
# print("--- Initial s1 ---")
# s1 = copy_class("Ali", ["math", "eng", "urdu"])
# s1.show()

# # 2. Create s_shallow using shallow_copy_object
# print("\n--- Shallow Copy Demonstration ---")
# s_shallow = s1.shallow_copy_object()
# print("s1:")
# s1.show()
# print("s_shallow:")
# s_shallow.show()

# # 3. Modify s_shallow's subject list (This will affect s1's list too)
# print("\nModifying s_shallow (shallow copy):")
# s_shallow.subjects = "sst_added_via_shallow"
# print("s1 (after s_shallow modification):")
# s1.show()
# print("s_shallow (after modification):")
# s_shallow.show()
# print("Notice how the Subject List IDs are the same and both lists changed.")

# print("\n" + "="*40 + "\n")

# # 4. Initialize another original object s2
# print("--- Initial s2 ---")
# s2 = copy_class("Mubeen", ["urdu", "math"])
# s2.show()

# # 5. Create s_deep using deep_copy_object
# print("\n--- Deep Copy Demonstration ---")
# s_deep = s2.deep_copy_object()
# print("s2:")
# s2.show()
# print("s_deep:")
# s_deep.show()

# # 6. Modify s_deep's subject list (This will *not* affect s2's list)
# print("\nModifying s_deep (deep copy):")
# s2.subjects = "Science_added_via_deep"
# print("s2 (after s_deep modification):")
# s2.show()
# print("s_deep (after modification):")
# s_deep.show()
# print("Notice how the Subject List IDs are different, and only s_deep's list changed.") # type: ignore