def  build_file(first,last,*user_info,):
    print(f"user_info{type(user_info)}")
    # user_info["first"] = first
    # user_info["last"] = last

    return user_info

user_file = build_file("wu",'小虎','四川',"高新")
print(user_file)
