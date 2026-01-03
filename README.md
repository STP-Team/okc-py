# Python обёртка для OKC API

Асинхронная обёртка для OKC API. Приватный пакет

## Установка

```bash
pip install git+https://github.com/STP-Team/okc-py.git
```

или

```bash
uv add git+https://github.com/STP-Team/okc-py.git
```

## Конфигурация

Конфигурация использует класс `Settings`:

```python
from okc_py import OKC, Settings

settings = Settings(
    BASE_URL="https://okc.example.com",
    REQUEST_TIMEOUT=30,
    RATE_LIMIT_ENABLED=True,
    REQUESTS_PER_SECOND=5.0,
)

async with OKC(settings=settings) as okc:
    pass
```

## Примеры

В директории `examples` лежат примеры использования пакета. Простой пример

## Репозитории

Клиент предоставляет доступ к следующим API репозиториям:

- `dossier` - API профайла (сотрудники, история должностей, показателей, ГОК)
- `premium` - API премиума (проценты выполнения премии, нормативы)
- `ure` - API URE (показатели)
- `sl` - API SL (Service Level)
- `tests` - API тестов (все тесты, назначенные сотрудникам тесты)
- `tutors` - API наставничества (наставники, стажеры, график)

## Обработка ошибок

```python
from okc_py import OKC
from okc_py.exceptions import (
    AuthenticationError,
    RateLimitError,
    NotFoundError,
    OKCError,
)


async def main():
    try:
        async with OKC() as okc:
            result = await okc.dossier.get(...)
    except AuthenticationError:
        print("Authentication failed")
    except RateLimitError as e:
        print(f"Rate limited, retry after {e.retry_after} seconds")
    except NotFoundError as e:
        print(f"Resource not found: {e.resource}")
    except OKCError as e:
        print(f"OKC API error: {e}")


asyncio.run(main())
```