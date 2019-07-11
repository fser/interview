import re

REGEX_TUPLE = r'(\S+) (\S+)$'

def get_file_content(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close

    #Discarding the header
    lines = lines[1:]
    return lines


def get_ips_dict():
    ip_dict = dict()
    lines = get_file_content("ips.dat")
    if lines == None :
        return None

    for line in lines:
        scan = re.match(REGEX_TUPLE, line)
        if scan :
            ip_dict[scan.group(2)] = scan.group(1)

    return ip_dict


def get_pps_dict():
    pps_dict = dict()
    lines = get_file_content("pps.dat")
    if lines == None:
        return None
    
    for line in lines:
        scan = re.match(REGEX_TUPLE, line)
        if scan:
            if pps_dict.get(scan.group(1)) == None:
                pps_dict[scan.group(1)] = 0
            pps_dict[scan.group(1)] += int(scan.group(2))

    return pps_dict 


def main():
    ip_dict = get_ips_dict()
    pps_dict = get_pps_dict()
    print(pps_dict)
    



if __name__ == "__main__":
    main()