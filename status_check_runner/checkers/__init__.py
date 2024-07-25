from __future__ import annotations

from abc import abstractmethod
from pathlib import Path

from pydantic import BaseModel


class Check(BaseModel):
    name: str
    command: str


class Checker:
    Config: type[BaseModel]

    @staticmethod
    @abstractmethod
    def get_checks(root_path: Path, config: Config) -> list[Check]:  # type: ignore  # noqa: F821
        """
        Return the list of checks required by this checker.

        Parameters
        ----------
            `root_path` (`Path`): The path to the root project directory.

            `config` (`Config`): The check configuration.

        Returns
        -------
            `list[Check]`: The checks required by this checker.
        """
