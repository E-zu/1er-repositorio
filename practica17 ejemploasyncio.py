import asyncio 
async def tarea(nombre):
    print(f"{nombre} inicia ")
    await asyncio.sleep(2)
    print (f"{nombre} termnia ")
async def main():
    await asyncio.gather(
        tarea("tarea1"),
        tarea("tarea2")
    )
asyncio.run(main())