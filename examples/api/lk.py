import asyncio
import logging
import os

from dotenv import load_dotenv

from okc_py import OKC

load_dotenv()
logging.basicConfig(level=logging.DEBUG)


async def main():
    async with OKC(
        username=os.getenv("OKC_USERNAME"), password=os.getenv("OKC_PASSWORD")
    ) as client:
        stat_history = await client.api.lk.get_stat_history(
            period="01.12.2025", stat_type_id=209
        )
        print(f"Result: {stat_history}")

        employee = await client.api.lk.get_employee(period="01.01.2026")
        print(f"Employee: {employee}")


if __name__ == "__main__":
    asyncio.run(main())
