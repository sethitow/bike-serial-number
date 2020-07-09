from __future__ import annotations
from dataclasses import dataclass
import datetime
import logging

LOG = logging.getLogger(__name__)

from bidict import bidict as Bidict

MODEL_CODE = Bidict(
    {
        "R": "RadRover",
        "M": "RadMini",
        "W": "RadWagon",
        "6": "RadCity 16",
        "9": "RadCity 19",
        "S": "RadCity Stepthru",
        "B": "RadBurro",
        "H": "RadRhino",
        "C": "Large Cargo Box",
        "K": "Small Cargo Box",
        "P": "Pedicab",
        "F": "Flatbed",
        "T": "Truckbed",
        "N": "Insulated Cargo Box",
        "Y": "Runner",
    }
)

MODEL_YEAR_CODE = Bidict({"A": 2018, "B": 2019, "C": 2020, "D": 2021})

FACTORY_CODE = Bidict({"F": "FactoryF", "V": "FactoryV"})

MONTH_CODE = Bidict(
    {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "O": 10,
        "N": 11,
        "D": 12,
    }
)


@dataclass
class Bike:
    """Holds data about a bike"""

    model: str
    model_year: int
    manufacture_month: int
    manufacture_year: int
    factory: str
    version: int
    serial_number: int

    @classmethod
    def from_serial_code(cls, serial_code: str) -> Bike:
        LOG.info(serial_code)
        try:
            model = MODEL_CODE.get(serial_code[0:1], None)
            model_year = MODEL_YEAR_CODE.get(serial_code[1:2], None)
            manufacture_month = MONTH_CODE.get(serial_code[2:3], None)
            manufacture_year = int(serial_code[3:5]) + 2000
            factory = FACTORY_CODE.get(serial_code[5:6], None)
            version = int(serial_code[6:7])
            serial_number = int(serial_code[7:])
        except ValueError as _:
            raise ValueError("Invalid Serial Code")
        return Bike(
            model=model,
            model_year=model_year,
            manufacture_month=manufacture_month,
            manufacture_year=manufacture_year,
            factory=factory,
            version=version,
            serial_number=serial_number,
        )

    def to_serial_code(self) -> str:
        raise NotImplementedError


if __name__ == "__main__":

    serial_codes = [
        "WBO19J101713",
        "SB419J100413",
        "RA118F100923",
        "MCO19J111815",
        "YD520V101061",
        "RB719F1000001",
        "HB719F1000001",
        "SB919F1000001",
    ]
    for code in serial_codes:
        myBike = Bike.from_serial_code(code)
        print(myBike)
