def matrix_chain_order(p):
    n = len(p) - 1  # تعداد ماتریس‌ها
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # آرایه برای ذخیره کمینه عملیات‌ها
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # آرایه برای ذخیره نقاط تقسیم



    for length in range(2, n + 1):  # طول زنجیره‌ها
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')  # مقدار اولیه برای کمینه‌سازی
            for k in range(i, j):  # تقسیم بازه
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  # ذخیره نقطه تقسیم

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])  # بخش اول
        print_optimal_parens(s, s[i][j] + 1, j)  # بخش دوم
        print(")", end="")


n =3
length = 2 , 3

length = 2
i = 1, 2
j = 2, 3

i , j = 1,2 
k = 1
m[1][2] = m[1][1]+m[2][2]+p[0]⋅p[1]⋅p[2]=0+0+10⋅20⋅30=6000


i , j = 2,3 
k = 2
m[2][3] = m[2][2]+m[3][3]+p[1]⋅p[2]⋅p[3]=0+0+20*30*40=24000



length = 3
i =1
j = 3
k = 1,2

k = 1
m[1][3]=m[1][1]+m[2][3]+p[0]⋅p[1]⋅p[3]=0+24000+10⋅20⋅40=32000
k= 2
m[1][3]=m[1][2]+m[3][3]+p[0]⋅p[2]⋅p[3]=6000+0+10⋅30⋅40=18000
