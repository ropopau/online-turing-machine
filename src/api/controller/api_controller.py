from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from service.api_service import ApiService
from models.machine_model import MachineModel


class ApiController(APIRouter):

    def __init__(self):
        super().__init__()
        self.api_service: ApiService = ApiService()

        self.add_api_route("/turing/{machine_name}", self.get_machine, methods=["GET"])
        self.add_api_route("/turing/create", self.create_machine, methods=["POST"])
        


    def get_machine(self, machine_name: str):
        machine: MachineModel = self.api_service.get_machine(machine_name=machine_name)
        return JSONResponse(status_code=200, content=machine.model_dump(mode="json"))
    
    def create_machine(self, machine: MachineModel) -> Response:
        self.api_service.create_machine(machine=machine)
        return Response()
    
    def execute_machine(self, machine_name: str):
        return Response()
    
    def link_machine(self, machine_name: str):
        return Response()