import asyncio

from okc_py import OKC


async def main():
    async with OKC(username="YOUR_USERNAME", password="YOUR_PASSWORD") as client:
        # Получить все тесты
        tests = await client.tests.get_tests()
        print(tests)

        # Получить назначенные тесты
        assigned_tests = await client.tests.get_assigned_tests(
            start_date="1.12.2025",
            stop_date="1.1.2026",
        )
        print(assigned_tests)

        # Получить пользователей из фильтров тестов
        test_users = await client.tests.get_users()
        print(test_users)

        # Получить супервайзеров из фильтров тестов
        test_supervisors = await client.tests.get_supervisors()
        print(test_supervisors)

        # Получить направления из фильтров тестов
        test_subdivisions = await client.tests.get_subdivisions()
        print(test_subdivisions)

        # Получить категории из фильтров тестов
        test_categories = await client.tests.get_categories()
        print(test_categories)


if __name__ == "__main__":
    asyncio.run(main())
