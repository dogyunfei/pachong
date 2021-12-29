import asyncio
import time


async def func1():
    print('你好啊,我叫潘金莲!')
    await asyncio.sleep(3)
    print('你好啊,我叫潘金莲！')


async def func2():
    print('你好啊,我叫王建国!')
    await asyncio.sleep(2)
    print('你好啊,我叫王建国！')


async def func3():
    print('你好啊,我叫李学勤!')
    await asyncio.sleep(4)
    print('你好啊,我叫李学勤！')

if __name__ == '__main__':
    f1=func1()
    f2=func2()
    f3=func3()
    tasks=[f1,f2,f3]
    t1=time.time()
    #一次性启动多个任务(协程)
    asyncio.run(asyncio.wait(tasks))
    t2=time.time()
    print(t2-t1)