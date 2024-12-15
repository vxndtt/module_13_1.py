import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    balls = [i for i in range(1,6)]
    for ball in balls:
        print(f'Силач {name} поднял шар {ball}')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    print('Старт')
    task1 = asyncio.create_task(start_strongman('Саша', 7))
    task2 = asyncio.create_task(start_strongman('Макс', 5))
    task3 = asyncio.create_task(start_strongman('Матвей', 10))
    await task1
    await task2
    await task3
    print('Финиш')

asyncio.run(start_tournament())
