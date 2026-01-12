from pydantic import BaseModel, Field


class StatLeaderboardEntry(BaseModel):
    """Single entry in the stat leaderboard."""

    employee_id: int = Field(alias="employeeId", description="Идентификатор сотрудника")
    fullname: str = Field(alias="fio", description="ФИО сотрудника")
    stat_value: float = Field(alias="statValue", description="Значение показателя")
    stat_rank: int = Field(
        alias="employeeRank", description="Ранг показателя сотрудника"
    )
    head: bool = Field(alias="head", description="Является ли сотрудник руководителем")


class StatLeaderboardResponse(BaseModel):
    """Response from get_stat_leaderboard endpoint."""

    root: list[StatLeaderboardEntry]


class EmployeeInformationEntry(BaseModel):
    """Single entry in the employee information list."""

    value: str | None = Field(description="Значение информации")
    name: str = Field(description="Название информации")


class EmployeeResponse(BaseModel):
    """Response from get_employee endpoint."""

    employee_id: int = Field(alias="employeeId", description="Идентификатор сотрудника")
    fullname: str = Field(alias="fio", description="ФИО сотрудника")
    post: str = Field(description="Должность")
    photo: str = Field(description="Имя файла фото")
    information: list[EmployeeInformationEntry] = Field(
        description="Дополнительная информация"
    )
    rg_detailed: bool = Field(alias="rgDetailed", description="Подробный флаг")
