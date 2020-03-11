from collections import defaultdict


def print_dict_sorted_by_value(header, d):

    print("==== {0} ====".format(header))
    sorted_list = sorted(d.items(), key=lambda kv: kv[1])
    for item in sorted_list:
        print("{0} = {1}".format(item[0], item[1]))

#
# Format
#   IP       - -    Time                           URL         Code Sz  Ref  UA                    XFF Tm  Loc

# 10.10.4.85 - - [01/Nov/2019:22:55:28 +0000] "GET / HTTP/1.1" 302 489 "-" "ELB-HealthChecker/2.0" "-" 108 "-"

# |<-------------- Part 1 ------------------->|<--- Part 2 ->|<-- P3 ->|4|5|<----- Part 6 ------>|7|8|<-P9>|10|
#


log_file = "/Users/shonsal/Downloads/access_log_pop-prod-gni-96cc4f7f5-wgj8f_11-01-2019.log"

ip_dict = defaultdict(int)
method_dict = defaultdict(int)
url_dict = defaultdict(int)
protocol_dict = defaultdict(int)
resp_code_dict = defaultdict(int)
time_taken_dict = defaultdict(int)

with open(log_file) as fp:

    # Split on double quote instead of space.
    for line in fp:
        line = line.rstrip()

        [part1, part2, part3, part4, part5, part6, part7, part8, part9, part10, unused] = line.split('"')

        # part1 will be '10.10.4.85 - - [01/Nov/2019:22:55:28 +0000]'
        # part2 will be 'GET / HTTP/1.1'
        # part3 will be ' 302 489 '
        # part4 will be '-' i.e. Referrer URL
        # part5 will be ''
        # part6 will be ELB-HealthChecker/2.0 i.e. User Agent
        # part7 will be ''
        # part8 will be '-'  i.e. X-Forwarded-For header
        # part9 will be '108'  i.e. Time Taken
        # part10 will be '-'  i.e. x-Location header

        # Now we can split each part on space

        # For debugging
        # print("[{0}]".format(part1))
        # print(part1.split(' '))
        [ip_addr, unused, unused, tm_stamp, millis] = part1.strip().split(' ')
        [method, url, protocol] = part2.strip().split(' ')
        [resp_code, resp_size] = part3.strip().split(' ')
        referrer = part4
        user_agent = part6
        xff_header = part8
        time_taken = int(part9)
        location_header = part10

        # X-Forwarded-for is a standard HTTP header and by default, is not logged by web server.
        # location header is application specific header

        ip_dict[ip_addr] = ip_dict[ip_addr] + 1
        method_dict[method] = method_dict[method] + 1
        url_dict[url] = url_dict[url] + 1
        protocol_dict[protocol] = protocol_dict[protocol] + 1
        resp_code_dict[resp_code] = resp_code_dict[resp_code] + 1

        if time_taken < 1000:
            time_taken_dict["0-1s"] += 1
        elif time_taken < 2000:
            time_taken_dict["1-2s"] += 1
        elif time_taken < 5000:
            time_taken_dict["2-5s"] += 1
        elif time_taken < 10000:
            time_taken_dict["5-10s"] += 1
        else:
            time_taken_dict[">10s"] += 1



print_dict_sorted_by_value("IP Addresses", ip_dict)
print_dict_sorted_by_value("HTTP Methods", method_dict)
print_dict_sorted_by_value("URLs", url_dict)
print_dict_sorted_by_value("Protocols", protocol_dict)
print_dict_sorted_by_value("Response Codes", resp_code_dict)
print_dict_sorted_by_value("Response Times", time_taken_dict)
