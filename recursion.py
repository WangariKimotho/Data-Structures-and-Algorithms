def to_string(n,base):
    convert_tString = '0123456789ABCDEF'
    if n < base:
        return convert_tString[n]
    else:
        return to_string(n//base,base) + convert_tString[n%base]

def recursive_list_sum(list_):
    total = 0
    for element in list_:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element
    return total

def non_neg_factorial(n):
    if n < 0:
        return False
    elif n==0 or n==1:
        factorial = 1
        return factorial
    else:
        return n * non_neg_factorial(n-1)

def recursive_fibonacci(n,memo={}):
    # Recursive fn using memoization to store the data as key,val
    # so as to extract the values from keys instead of duplicating calculations
    # that essentially give the same result over and over
    # we initialize a memo dict with the keys being arg to fn, val will be return val

    if n in memo:  # is n a key in memo
        return memo[n]  # if so return its val
    if n==1 or n==2:
        return 1
    else:
        memo[n] = recursive_fibonacci(n-1, memo) + recursive_fibonacci(n-2, memo)
        return memo[n]

def sum_digits(n):
    # n = str(n)
    # if len(n) < 0:
    #     return False
    # elif len(n)==1:
    #     return n
    # else:
    #     for i in range(len(n)+1):
    #         return int(sum_digits(n[i])) + int(sum_digits(n[i+1:]))
    if n==0:
        return 0
    else:
        return n%10 + sum_digits(int(n/10))

def sum_series(n):
    if n-2<=0:
        return n
    return n+sum_series(n-2)

def harmonic_sum(n):
    # counter = 1
    # sum = 0
    # for i in range(1,n+1):
    #     sum += 1/counter
    #     counter+=1
    #return sum
    if n==1:
        return 1
    else:
        return harmonic_sum(n-1)+ 1/n

def geometric_sum(n):
    if n<0:
        return 0
    else:
        return 1 / (pow(2,n)) + geometric_sum(n-1)
def power(a,b):
    # return power(a,b)
    if a==0:
        return 0
    elif b==0:
        return 1
    elif b==1:
        return a
    else:
        return a* power(a,b-1)

def gcd(a,b):
    low = min(a,b)
    high = max(a,b)
    if low == 0:
        return high
    elif low ==   1:
        return 1
    else:
        return gcd(low,high%low)

def grid_traveler(m,n, memo={}) :
    """
    :param m: represents the rows
    :param n: represents the columns
    :param memo: dict to store the results to leverage memoization
    :return: int number of ways to travel through m*n grid
    """

    tuple_ = (m,n)
    if tuple_ in memo:  # check if the args are in memo ie memo fetching logic
        return memo[tuple_]  # return the vals
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[tuple_] =  grid_traveler(m-1,n,memo) + grid_traveler(m,n-1,memo)
    return memo[tuple_]

def canSum(targetSum:int, arr:list,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return True
    if targetSum < 0:
        return False

    for num in arr:
        remainder = targetSum - num
        if canSum(remainder,arr,memo):
            memo[targetSum]=True
            return True

    memo[targetSum] = False
    return False

def how_sum(target_sum,numbers,memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum==0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder,numbers,memo)
        if result is not None:
            memo[target_sum] = result + [num]
            return memo[target_sum]

    memo[target_sum]=None
    return None


def best_sum(target_sum,numbers,memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum==0:
        return []
    if target_sum<0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        result = best_sum(remainder,numbers,memo)
        if result is not None:
            combination = result.copy() + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return memo[target_sum]


def can_construct(target, word_bank,memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix,word_bank):
                memo[target] = True
                return True
    memo[target] = False
    return memo[target]

def count_construct(target,word_bank,memo={}):
    if target in memo:
        return memo[target]
    if target=='':
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            memo[target] = count_construct(suffix,word_bank,memo)
            total_count += memo[target]

    #memo[target] = total_count
    return total_count

def all_construct(target, word_bank,memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    results = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix,word_bank,memo)
            if suffix_ways:
                target_ways = map(lambda suffix_ways:[word,*suffix_ways],suffix_ways)
                results.extend(target_ways)

    memo[target] = results
    return memo[target]

#print(to_string(18,16))
#print(recursive_list_sum([1, 2, [3,4], [5,6]]))
#print(non_neg_factorial(4))
#print(recursive_fibonacci(6))
#print(sum_digits(97))
#print(sum_series(9))
#print(harmonic_sum(4))
#print(geometric_sum(4))
#print(power(4,3))
#print(gcd(12,24))

# print(grid_traveler(1,1))
# print(grid_traveler(1,0)) # grid_traveler(m,n)==grid_traveler(n,m)
# print(grid_traveler(3,7))
# print(grid_traveler(4,3))
# print(grid_traveler(18,18))

# print(canSum(7,[2,3]))
# print(canSum(7,[5,3,4,7]))
# print(canSum(7,[2,2,1]))
# print(canSum(8,[2,3]))
# print(canSum(11,[4,5]))
# print(canSum(7,[2,4]))
# print(canSum(10,[0,9]))

#print(howSum(7,[2,3]))
#print(howSum(17,[5,3,4,7]))
# print(howSum(33,[2,2,2]))
# print(howSum(8,[2,3]))
# print(howSum(11,[4,5]))
# print(howSum(41,[2,4]))
# print(howSum(300,[7,14]))

# print(best_sum(7,[5,3,4,7]))
# print(best_sum(8,[2,3,5]))
# print(best_sum(11,[1,5,4]))
# print(best_sum(100,[1,2,5,25]))

# print(can_construct('abcdef',['ab','abc','cd','def','abcd']))
# print(can_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
# print(can_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
# print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeeeeee']))

#print(count_construct('purple',['purp','p','ur','le','purpl']))
#print(count_construct('abcdef',['ab','abc','cd','def','abcd']))
# print(count_construct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
# print(count_construct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
# print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeee','eeeee','eeeeeeeee']))

print(all_construct('purple',['purp','p','ur','le','purpl']))
print(all_construct('abcdef',['ab','abc','cd','def','abcd','ef','c']))
#print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz',['a','aa','aaaa','aaaaaa']))

