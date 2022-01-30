# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
# interval
def merge_tuples(tuples_list):

    # Input: tuples_list is a list of tuples of denoting intervals
    # Output: a list of tuples sorted by ascending order of the size of
    # the interval
    # if two intervals have the size then it will sort by the
    # lower number in the interval


    for i in range(len(tuples_list)-1):
        for j in range(i, len(tuples_list)):
    # comparing the adjacent elements
            if tuples_list[i][1] > tuples_list[j][1]:
    # swapping
                tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]
    return tuples_list


def sort_by_interval_size(tuples_list):


    for i in range(len(tuples_list)-1):
        for j in range(i, len(tuples_list)):
    # comparing the adjacent elements
            dif1 = tuples_list[i][1]-tuples_list[i][0]
            dif2 = tuples_list[j][1]-tuples_list[j][0]
            if dif1 > dif2:
    # swapping
                tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]
    return tuples_list

def main():


    # open file intervals.in and read the data and create a list of tuples
    fileIn = open("interval.in", "r")
    num_records = fileIn.readline().rstrip()
    tuples_list = []
    line = fileIn.readline().rstrip()
    while line:
        values = line.split(" ")
        tuples_list.append((int(values[0]), int(values[1])))
        line = fileIn.readline().rstrip()
    fileIn.close()
    fileOut = open("interval.out", "w")
# merge the list of tuples
    mrgTuple = merge_tuples(tuples_list)
    fileOut.write(str(mrgTuple))
    fileOut.write("\n")
# sort the list of tuples according to the size of the interval
    sortTuple = sort_by_interval_size(tuples_list)
    fileOut.write(str(sortTuple))
    fileOut.close()
# run your test cases
'''
print (test_cases())
'''


if __name__ == "__main__":
    main()
