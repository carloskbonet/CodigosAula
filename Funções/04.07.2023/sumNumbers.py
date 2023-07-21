def sumNumbers(value: int):
    stop = int(value + 1);
    result = int(0);

    for i in range(1, stop, 1):
        result = result + i;

    return result;