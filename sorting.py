def sort_list(number_list):
    for i in range (len(number_list)):
        for j in range(i + 1, len(number_list)):
            if(number_list[i] > number_list[j]):
                temp = number_list[i]
                number_list[i] = number_list[j]
                number_list[j] = temp

    return number_list

if __name__ == "__main__":
    number_list = [11,21,1,23,5,2,8,10,3,6435,4]
    sorted_list = sort_list(number_list)
    print(sorted_list)