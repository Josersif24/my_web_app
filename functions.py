FILEPATH ='todos.txt'
def get_file(filepath=FILEPATH ):
    """ this function fp what it has to do """
    with open(filepath, 'r') as file:
        l_todos = file.readlines()
    return l_todos
def write_list(list, file_path=FILEPATH ):
    """ this one also do what to to do """
    with open(file_path,'w') as l_file:
        l_file.writelines(list)



if __name__ =="__main__":
    print(f"insideIf{__name__}")
    print("helo from function")