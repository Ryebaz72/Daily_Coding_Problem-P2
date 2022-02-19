def product_array(input_array):
    list_len = len(input_array)
    a = 0
    b = list_len
    output_array = []
    while a < list_len:
        output_array.insert(a, 1)
        for x in range(b):
            if x == a:
                continue
            else:
                output_array[a] = output_array[a] * input_array[x]
        a += 1
    return output_array

if __name__ == '__main__':
    input_array = [1, 2, 3, 4, 5]
   # input_array = [3, 2, 1]
    output_array = product_array(input_array)
    print(output_array)