# T: The number of test case
T: int = int(input())
# N: The number of documents / M: Finding the document's order
for _ in range(T):
    N, M = map(int,input().split())

    doc_num = list(range(N))
    importance = list(map(int,input().split()))
    
    num = 1
    result = False
    while not result:
        dn = doc_num[0]
        imp = importance[0]

        if dn == M:
            if imp >= max(importance):
                print(num)
                result = True
            else:
                doc_num = doc_num[1:]
                doc_num.append(dn)
                importance = importance[1:]
                importance.append(imp)
        else:
            if imp >= max(importance):
                num += 1
                doc_num = doc_num[1:]
                importance = importance[1:]
            else:
                doc_num = doc_num[1:]
                doc_num.append(dn)
                importance = importance[1:]
                importance.append(imp)
