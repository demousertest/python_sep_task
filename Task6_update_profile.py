user_profile = {}

for i in range(0,4):
    input_field = input("enter field name : ")
    input_val = input("enter field name : ")
    user_profile[f"{input_field}"] =  input_val

print(user_profile)

def edit_profile(args):
    input_field = input("enter field name : ")
    input_val = input("enter field name : ")
    args[f"{input_field}"] =  input_val
    return args
edit_profile(user_profile)
user_profile