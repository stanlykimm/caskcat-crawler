import motor.motor_asyncio
from bson import ObjectId
from fastapi.logger import logger
from motor.core import Collection
from pymongo import monitoring

class MongoDB:
    def __init__(self):
        self.__client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:kyhs1167!!@localhost:27017/?authMechanism=DEFAULT')
        self.__db = self.__client.caskcat
        self.__product: Collection = self.__db.product
        self.__brand: Collection = self.__db.brand
        self.__dailyshot: Collection = self.__db.dailyshot

    @property
    def product(self) -> Collection:
        return self.__product

    @property
    def brand(self) -> Collection:
      return self.__brand

    @property
    def dailyshot(self) -> Collection:
      return self.__dailyshot

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class CommandLogger(monitoring.CommandListener):
    def started(self, event):
        logger.info(
            "Command {0.command_name} with request id "
            "{0.request_id} started on server "
            "{0.connection_id}".format(event)
        )

    def succeeded(self, event):
        logger.info(
            "Command {0.command_name} with request id "
            "{0.request_id} on server {0.connection_id} "
            "succeeded in {0.duration_micros} "
            "microseconds".format(event)
        )

    def failed(self, event):
        logger.info(
            "Command {0.command_name} with request id "
            "{0.request_id} on server {0.connection_id} "
            "failed in {0.duration_micros} "
            "microseconds".format(event)
        )


class TopologyLogger(monitoring.TopologyListener):
    def opened(self, event):
        logger.info("Topology with id {0.topology_id} opened".format(event))

    def description_changed(self, event):
        logger.info("Topology description updated for topology id {0.topology_id}".format(event))
        previous_topology_type = event.previous_description.topology_type
        new_topology_type = event.new_description.topology_type
        if new_topology_type != previous_topology_type:
            logger.info(
                "Topology {0.topology_id} changed type from "
                "{0.previous_description.topology_type_name} to "
                "{0.new_description.topology_type_name}".format(event)
            )

    def closed(self, event):
        logger.info("Topology with id {0.topology_id} closed".format(event))


class HeartbeatLogger(monitoring.ServerHeartbeatListener):
    def started(self, event):
        logger.info("Heartbeat sent to server {0.connection_id}".format(event))

    def succeeded(self, event):
        logger.info(
            "Heartbeat to server {0.connection_id} "
            "succeeded with reply "
            "{0.reply.document}".format(event)
        )

    def failed(self, event):
        logger.warning(
            "Heartbeat to server {0.connection_id} failed with error {0.reply}".format(event)
        )


mongodb = MongoDB()
