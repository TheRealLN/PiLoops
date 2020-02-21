from time import time

# Grabs up to the first n digits of pi from the file location (not including
# the '3.')
def read_pi(filename, n):
    pi_file = open(filename, 'r')
    # Moves to first digit after decimal
    pi_file.seek(2,0)
    pi_str = pi_file.read(n)
    pi_file.close()
    return pi_str

# Prints the dictionary in a list-like fashion
def print_list_dict(loop_dict, orig_n):
    if loop_dict is None:
        return
    n = orig_n
    print(str(n))
    for i in range(len(loop_dict)):
        n = loop_dict.get(n, -1)
        if n == -1:
            break
        print(" -> " + str(n))
    return

# Finds the index where a number occurs in pi
# indexing is for what index system to use, usually 0 or 1 based
def find_index(pi_str, n, indexing):
    match = True
    str_n = str(n)
    # Indexing based on 1
    indx = indexing
    while True:
        # Remove -1 if 0 indexing, and vice versa for 1 indexing
        try:
            ch = pi_str[indx - indexing]
        except:
            return -1
        # Tests if first character of string is present
        if ch == str_n[0]:
            # Tests if entire string is present
            for i in range(1, len(str_n)):
                try:
                    ch = pi_str[indx - indexing + i]
                except:
                    return -1
                if ch != str_n[i]:
                    match = False
                    break
            if match == True:
                return indx
            match = True
        indx += 1

    # Never should reach this point
    return -1


# Returns dictionary of values if any loop exists
# Also returns flag: Returns 0 if no loop exists for pi_str, -1 if 'invalid
# loop', 1 if proper loop
def pi_number_loop(pi_str, orig_n, indexing):
    n = orig_n
    # Creates a dictionary that allows O(1) avg lookup time, with O(2n) -> O(n)
    # storage space
    # In hindsight, a list would have been simpler, as no loop within a
    # reasonable range of pi is
    # sufficiently large to benefit from this runtime consideration
    loop_dict = {}

    # Constrcts the dictionary
    while True:
        # Finds index of n
        indx = find_index(pi_str, n, indexing)
        if indx == -1:
            return None, 0
        
        # Adds number to dictionary
        loop_dict[n] = indx

        # Tests if any loop occurs
        loop_value = loop_dict.get(indx, -1)
        if loop_value != -1:
            # Tests for original number being the index
            if indx == orig_n:
                return loop_dict, 1
            # Original value is not the index (loop occurs somewhere else)
            return loop_dict, -1

        # Updates n to be the index
        n = indx
        continue

    # Never should reach this point
    return None, 0


# Prints out the 169 loop shown in Numberphile's video:
# https://www.youtube.com/watch?v=W20aT14t8Pw
def main():
    digits = 1000000
    num = 169
    indexing = 1

    # Reads pi from file
    start_time = time()
    pi_str = read_pi("pi_million_digits.txt", digits)
    end_time = time()
    seconds = end_time - start_time
    if pi_str == '':
        print('Could Not read pi from file.')
        exit(1)
    else:
        print("{} digits of pi read in {} seconds.".format(digits, seconds))

    # Finds a loop at num using indexing, if one exists
    loop_dict, flag = pi_number_loop(pi_str, num, indexing)
    if flag != 1:
        print('No proper loop found.')
    else:
        print_list_dict(loop_dict, num)

if __name__ == '__main__':
    main()