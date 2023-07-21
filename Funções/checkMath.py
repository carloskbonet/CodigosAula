def isParOrImpar(number: int):
    calc = int(0);
    result = (str);

    calc = number % 2;

    if ( calc == 0 ):
        result = "O número digitado é PAR";
    else:
        result = "O número digitado é IMPAR";

    return result;