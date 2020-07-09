import logging

import graphene as g
import serial_number

LOG = logging.getLogger(__name__)

class Bike(g.ObjectType):
    model = g.String()
    model_year = g.Int()
    manufacture_month = g.Int()
    manufacture_year = g.Int()
    factory = g.String()
    version = g.Int()
    serial_number = g.Int()


class BikeInput(g.InputObjectType):
    model = g.String(required=True)
    model_year = g.Int(required=True)
    manufacture_month = g.Int(required=True)
    manufacture_year = g.Int(required=True)
    factory = g.String(required=True)
    version = g.Int(required=True)
    serial_number = g.Int(required=True)


class Query(g.ObjectType):
    bike_info = g.Field(Bike, serial_code=g.String(required=True))

    bike_serial_code = g.Field(g.String, bike=BikeInput())

    def resolve_bike_info(root, info, serial_code):
        LOG.info(type(serial_code))
        bike = serial_number.Bike.from_serial_code(serial_code)
        return Bike(
            model=bike.model,
            model_year=bike.model_year,
            manufacture_month=bike.manufacture_month,
            manufacture_year=bike.manufacture_year,
            factory=bike.factory,
            version=bike.version,
            serial_number=bike.serial_number,
        )

    def resolve_bike_serial_code(root, info, bike):
        the_bike = serial_number.Bike(
            model=bike.model,
            model_year=bike.model_year,
            manufacture_month=bike.manufacture_month,
            manufacture_year=bike.manufacture_year,
            factory=bike.factory,
            version=bike.version,
            serial_number=bike.serial_number,
        )
        return the_bike.to_serial_code()


schema = g.Schema(query=Query)
