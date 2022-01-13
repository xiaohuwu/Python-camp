def permutations(param):
    if len(param) == 1: return set(param)
    first = param[0]
    rest = permutations(param[1:])
    result = set()
    print("result----------->")
    print(','.join(result))

    print("rest----------->")
    print(','.join(rest))
    for p in rest:
        for i in range(0, len(param)):
            print("i: " + str(i))
            print("p[0:i]:" + p[0:i] + ",first:" + first + ",p[i:]:" + p[i:])
            remain = p[0:i] + first + p[i:]
            print("remain:" + remain)
            result.add(remain)
    print("result:" + ','.join(result), "\n>>>>>>>>>")
    return result


permutations('aba')
