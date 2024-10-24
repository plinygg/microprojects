def scramble(arr):
    def dfs(arr):
        if len(arr) == 0:
            return [[]]
        
        ret = []
        sub = dfs(arr[1:])
        for value in sub:
            for i in range(len(value)+1):
                copy = value.copy()
                copy.insert(i, arr[0])
                ret.append(copy)
        return ret

    res = []
    temp = dfs(arr)
    
    for value in temp:
        res.append("".join(value)) 
    return res


        

def main():
    an = input('Input a string you would like to see every single anagram of.\n')
    print('-------\nHere is every single anagram:')
    temp = scramble(an)
    
    for val in temp:
        print(val)
    print('There are {a} anagrams that you can make from your input \"{b}\".'.format(a=len(temp),b=an))
    again = input('Would you like to input another word? Y/n: ')
    again.lower()
    if again == "y":
        main()
    else:
        print('Thank you for using the anagram maker.')
        return

main()
