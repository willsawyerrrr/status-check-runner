from __future__ import annotations

from abc import abstractmethod

from pydantic import BaseModel


class Check(BaseModel):
    name: str
    command: str


class Checker:
    Config: type[BaseModel]

    @staticmethod
    @abstractmethod
    def get_checks(config: Config) -> list[Check]:  # type: ignore  # noqa: F821
        """
        Return the list of checks required by this checker.

        Parameters
        ----------
            `config` (`Config`): The check configuration.

        Returns
        -------
            `list[Check]`: The checks required by this checker.
        """
