import logging

from ...client import Client
from ..models.lk import EmployeeResponse, StatLeaderboardResponse
from .base import BaseAPI

logger = logging.getLogger(__name__)


class LkAPI(BaseAPI):
    """HTTP API for LK endpoints.
    TODO Добавить выгрузку доступных показателей."""

    def __init__(self, client: Client):
        """Initialize LK API repository.

        Args:
            client: Authenticated OKC API client
        """
        super().__init__(client)
        self.service_url = "newlk/api"

    async def get_report(
        self,
        period: str,
        employee_id: str | int | None,
    ):
        """Получить отчет по показателю сотрудника.

        Args:
            period: Период выгрузки отчета. В формате 1.12.2025
            employee_id: Идентификатор сотрудника
                         Если None - получает отчет по авторизованному сотруднику

        Returns:
            Отчет по показателю сотрудника
        """
        data = {
            "employeeId": employee_id,
            "period": period,
        }
        response = await self.post(f"{self.service_url}/get-report", data=data)

        try:
            result = await response.json()
            return result
        except Exception as e:
            logger.error(f"[Линии] Ошибка получения отчета: {e}")
            return None

    async def get_report_history(self, employee_id: str | int | None = None):
        """Получает историю отчетов сотрудника

        Args:
            employee_id (str | int | None): ID сотрудника

        Returns:
            ReportHistoryResponse | None: История отчетов сотрудника
        """
        data = {
            "employeeId": employee_id,
        }
        response = await self.post(f"{self.service_url}/get-report-history", data=data)

        try:
            result = await response.json()
            return result
        except Exception as e:
            logger.error(f"[Линии] Ошибка получения истории отчетов: {e}")
            return None

    async def get_employee(self, period: str, employee_id: str | int | None = None):
        """Получает информацию о сотруднике

        Args:
            period (str): Период отчета
            employee_id (str | int | None): ID сотрудника
                Если не указан, возвращает информацию об авторизованном пользователе

        Returns:
            EmployeeResponse | None: Информация о сотруднике
        """
        data = {
            "period": period,
            "employeeId": employee_id,
        }
        response = await self.post(f"{self.service_url}/get-employee", json=data)

        try:
            result = await response.json()
            return EmployeeResponse.model_validate(result)
        except Exception as e:
            logger.error(f"[Линии] Ошибка получения информации о сотруднике: {e}")
            return None

    async def get_stat_leaderboard(
        self, period: str, stat_type_id: int
    ) -> StatLeaderboardResponse | None:
        """Получает лидерборд показателя сотрудника

        Args:
            period (str): Период отчета
            stat_type_id (int): ID показателя

        Returns:
            StatLeaderboardResponse | None: Отчет по показателю сотрудника
        """
        data = {
            "period": period,
            "statTypeId": stat_type_id,
        }
        response = await self.post(
            f"{self.service_url}/get-stat-leaderboard", data=data
        )

        try:
            result = await response.json()
            return StatLeaderboardResponse.model_validate({"root": result})
        except Exception as e:
            logger.error(f"[Линии] Ошибка получения лидерборда показателя: {e}")
            return None

    async def get_stat_history(
        self, period: str, stat_type_id: int, employee_id: str | None = None
    ):
        """Получает историю показателя сотрудника

        Args:
            period (str): Период отчета
            stat_type_id (int): ID показателя
            employee_id (str | None): ID сотрудника

        Returns:
            StatHistoryResponse | None: Отчет по показателю сотрудника
        """
        data = {
            "period": period,
            "statTypeId": stat_type_id,
            "employeeId": employee_id,
        }
        response = await self.post(f"{self.service_url}/get-stat-history", json=data)

        try:
            result = await response.json()
            return result
        except Exception as e:
            logger.error(f"[Линии] Ошибка получения истории показателя: {e}")
            return None
