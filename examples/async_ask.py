import asyncio
from brave_leo import AsyncLeo

leo = AsyncLeo()

async def main():
    # It initially contains Brave's specified System Prompt.
    response = leo.ask('What is the weather like today?')
    print(response.completion)

    # You can use it as Llama by explicitly leaving System Prompt empty.
    response = leo.ask('What is the weather like today?', system_prompt='')
    print(response.completion)

    await leo.close()

asyncio.run(main())