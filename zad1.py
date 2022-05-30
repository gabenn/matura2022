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

def permutation(n, A=[]):
    k = 0
    for a in A:
        if 1<=a<=n:
            for j in range(n):
                if j+1 not in A:
                    print(A, A.index(a), j)
                    A[A.index(a)] = j+1
                    k += 1

    return [k,A]   

  
print(permutation(4, [8,9,6,1]))