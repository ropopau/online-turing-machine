from models.machine_model import MachineModel
from repository.api_repository import ApiRepository

class ApiService():

    def __init__(self):
        self.repository: ApiRepository = ApiRepository()


    def get_machine(self, machine_name: str) -> MachineModel:
        return self.repository.get_machine(machine_name=machine_name)
    
    def create_machine(self, machine: MachineModel) -> None:
        self.repository.add_machine(machine=machine)
