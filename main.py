def print_fibonacci(n):
    a, b = 0, 1
    count = 0  # 添加计数器
    for _ in range(n):
        print(a, end=' ')
        count += 1  # 增加计数器
        if count % 3 == 0:  # 每3个数字换一行
            print()  # 添加换行符
        a, b = b, a + b

# 调用函数打印前100个斐波那契数
print_fibonacci(100)