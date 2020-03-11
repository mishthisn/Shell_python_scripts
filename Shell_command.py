# 100-199
# 200-399
# 400-500
# 1. Open the file and print the first line

compnay_server_log_array = ["Ip","Date","UserNo","page","ResponseCode","No","Time"]

def find_duplicate_array(actual_array, expected_array):
    found_item = 0
    for item in actual_array:
        if item in expected_array:
            found_item += 1
            print("Duplicate item")
        else:
            print("Not found")
#csv_reader = csv.reader(f, delimiter=",")

def compare_length(actual_array_length, expected_array_length):
    if actual_array_length != expected_array_length:
        return True
    else:
        return False

#def compare_array_elements(actual_array, expected_array):




with open("server_log_file") as fp:
    hearder_line = fp.readline()
    print(hearder_line)
    header_array = hearder_line.split(',')
    print(header_array)


#compare_length((len(header_array), len(compnay_server_log_array))

find_duplicate_array(header_array, compnay_server_log_array)

