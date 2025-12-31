"""Data models for OKC API."""

from .dossier import Employee, EmployeeData
from .premium import SpecialistPremiumResponse, HeadPremiumResponse
from .sl import ReportData, SlRootModel

__all__ = [
    "Employee",
    "EmployeeData",
    "SpecialistPremiumResponse",
    "HeadPremiumResponse",
    "ReportData",
    "SlRootModel",
]
