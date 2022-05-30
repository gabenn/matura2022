# def permutation(n, A=[]):
#     if len(A) == n:
#         print(A)
#     else:
#         for i in range(n):
#             if i not in A:
#                 A.append(i)
#                 permutation(n, A)
#                 A.pop()
#     return A

# print(permutation(3))

def permutation(n, A=[]):
    k = 0
    for a in A:
        if not 1<=a<=n:
            for j in range(n):
                if j + 1 not in A:  
                    A[A.index(a)] = j + 1   
                    k += 1
                    break     
    return [k,A]   

print(permutation(4, [8,9,6,1]))