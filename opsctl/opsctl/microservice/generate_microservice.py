from opsctl.utility import my_utilities

def generate(microservice, name):
    print("\n")
    print("Inside microservice --> generate")
    my_utilities.create_folder(name)
    my_utilities.copy_sourcecode_folder(microservice, name)

