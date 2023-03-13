requirements = []
with open("requirements.txt") as file_obj:
    requirements = file_obj.readlines()
    requirements = "".join(requirements).split("\n")
    print(requirements)
    requirements = [req.replace("\n","") for req in requirements]
    print(requirements)