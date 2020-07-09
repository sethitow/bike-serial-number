from serial_number import Bike


def test_decode_serial_number0():
    myBike = Bike.from_serial_code("WBO19J101713")
    assert myBike == Bike(
        model="RadWagon",
        model_year=2019,
        manufacture_month=10,
        manufacture_year=2019,
        factory=None,
        version=1,
        serial_number=1713,
    )


def test_decode_serial_number1():
    myBike = Bike.from_serial_code("RA118F100923")
    assert myBike == Bike(
        model="RadRover",
        model_year=2018,
        manufacture_month=1,
        manufacture_year=2018,
        factory="FactoryF",
        version=1,
        serial_number=923,
    )


def test_decode_serial_number2():
    myBike = Bike.from_serial_code("YD520V101061")
    assert myBike == Bike(
        model="Runner",
        model_year=2021,
        manufacture_month=5,
        manufacture_year=2020,
        factory="FactoryV",
        version=1,
        serial_number=1061,
    )
