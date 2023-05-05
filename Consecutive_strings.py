def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for i in range(len(strarr) - k + 1):
            s = ''.join(strarr[i:i+k])
            if len(s) > len(result):
                result = s

    return result


    

k=int(input("Enter number: "))
starr=[str(i) for i in input("Enter names: ").split()]
print(longest_consec(starr, k))
