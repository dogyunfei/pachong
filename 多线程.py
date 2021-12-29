# #单线程程序
# def func():
#     for i in range(1000):
#         print('func',i)
# if __name__ == '__main__':
#     func()
#     for i in range(1000):
#         print('main',i)


# from threading import Thread
# def func():
#     for i in range(1000):
#         print('func',i)
#
# if __name__ == '__main__':
#     t=Thread(target=func)
#     t.start()   #多线程状态为开始工作状态，具体的执行时间由cpu决定
#     T2=Thread(target=func)
#     T2.start()
#     for i in range(1000):
#         print('main', i)
from threading import Thread
class Mythread(Thread):
    def run(self):
        for i in range(1000):
            print('子线程',i)

if __name__ == '__main__':
    t=Mythread()
    t.start()
    for i in range(1000):
        print('主线程',i)

