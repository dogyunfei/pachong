from multiprocessing import Process


def func():
    for i in range(10000):
        print('子进程', i)



if __name__ == '__main__':
    P = Process(target=func)
    P.start()
    for i in range(10000):
        print('主进程', i)


