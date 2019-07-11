import re

def get_file_content(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close

    #Discarding the header
    lines = lines[1:]
    return lines


def get_ips_list():
    ip_dict = dict()
    lines = get_file_content("ips.dat")
    if lines == None :
        return None

    for line in lines:
        scan = re.match(r"(\S+) (\S+)$", line)
        if scan :
            ip_dict[scan.group(2)] = scan.group(1)

    return ip_dict
        


def main():
    print(get_ips_list())
    



if __name__ == "__main__":
    main()