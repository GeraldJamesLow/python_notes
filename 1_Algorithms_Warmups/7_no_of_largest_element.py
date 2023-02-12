
#* Count how many of the tallest candles (largest elements) there are

a = [1,2,3,5,3,6,2,6,1,4,5]


def birthdayCakeCandles(candles):
    # Write your code here
    largest_element = 0
    l_element_counter = 0
    for candle_number in range(len(candles)):
        if largest_element < candles[candle_number]:
            largest_element = candles[candle_number]
            l_element_counter = 1
        elif largest_element == candles[candle_number]:
            l_element_counter += 1
        else:
            continue
    return 'largest element', largest_element,'counter:', l_element_counter

#! Altered the return statement to return largest element and its count

print(birthdayCakeCandles(a))