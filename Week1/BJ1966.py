# T: The number of test cases
T: int = int(input())
# N: The number of documents / M: Finding the document's order
for _ in range(T):
    N, M = map(int,input().split())

    doc_num = list(range(N))
    importance = list(map(int,input().split()))
    
    num = 1
    result = False
    while not result and len(importance) > 0:
        document_number = doc_num[0]
        important = importance[0]

        if document_number == M:
            if important >= max(importance):
                print(num)
                result = True
            else:
                doc_num.pop(0)
                doc_num.append(document_number)
                importance.pop(0)
                importance.append(important)
        else:
            if important >= max(importance):
                num += 1
                doc_num.pop(0)
                importance.pop(0)
            else:
                doc_num.pop(0)
                doc_num.append(document_number)
                importance.pop(0)
                importance.append(important)
