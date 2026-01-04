import asyncio

from okc_py import OKC


async def main():
    async with OKC(username="YOUR_USERNAME", password="YOUR_PASSWORD") as client:
        filters = await client.appeals.get_filters()
        print(f"Filters: {filters}")

        appeals_by_city = await client.appeals.get_appeals_by_city(
            unit="7", interval="60"
        )
        print(f"Appeals by city: {appeals_by_city}")

        details_by_city = await client.appeals.get_details_by_city(
            unit="7", interval="60", city="447", problem_class="19133"
        )
        print(f"Details by city: {details_by_city}")

        appeals_by_problem = await client.appeals.get_appeals_by_problem(
            unit="7", interval="60"
        )
        print(f"Appeals by problem: {appeals_by_problem}")

        details_by_problem = await client.appeals.get_details_by_problem(
            unit="7", interval="60", city="553", problem_class="19133"
        )
        print(f"Details by problem: {details_by_problem}")


if __name__ == "__main__":
    asyncio.run(main())
