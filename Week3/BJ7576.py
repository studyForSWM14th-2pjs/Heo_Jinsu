# M (Column), N (Row) : Shape of box
M, N = map(int,input().split())

# �丶�� ���� ���� - 0:���� ���� �丶�� | 1: ���� �丶�� | -1: �丶�� ����
tomatos = list()
for i in range(N):
    tomatos.append(list(map(int,input().split())))

days = 0

# Ǫ�� ��...