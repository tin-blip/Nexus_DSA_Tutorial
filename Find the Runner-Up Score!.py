if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

    
    #remove duplicates
unique_scores = list(set(arr))

#sort in ascending order
unique_scores.sort()

#second highest
print(unique_scores[-2])
