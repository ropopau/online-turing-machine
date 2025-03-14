from pymongo import MongoClient
from models.machine_model import MachineModel


class ApiRepository():


    def __init__(self, user: str = "otms_admin"):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['otms']
        self.users_collection = self.db["collection_" + user]

    def get_machine(self, machine_name: str) -> MachineModel:
        return MachineModel(**self.users_collection.find_one({"name": machine_name}))


    def add_machine(self, machine: MachineModel):
        self.users_collection.insert_one(machine.model_dump())