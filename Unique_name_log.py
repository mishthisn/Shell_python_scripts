unique_dict = {}

with open("log_file.txt") as fp:
    file_first_line = fp.readline()
    print("Printing first line: ",file_first_line)
    #file_first_line_array = file_first_line.split(",")
    #print(file_first_line_array)

    #file_content = fp.read()
    #file_content_array = file_content.split(",")
    #print(file_content)
    #print(file_content_array)

    for file_line in fp:
        file_line_array = file_line.split(",")
        #print(file_line_array)
        #file_column_URL = file_line_array[0]
        #file_column_Date_time = file_line_array[1]
        file_column_User_Name = file_line_array[2]

        print(file_column_User_Name)
        if file_column_User_Name not in unique_dict:
            unique_dict[file_column_User_Name] = 1
        else:
            unique_dict[file_column_User_Name] += 1

    lenght_dict = len(unique_dict.keys())
    print(lenght_dict)
    print(unique_dict)



