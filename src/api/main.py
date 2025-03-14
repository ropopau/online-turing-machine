import fastapi
from controller.api_controller import ApiController

"""

POST CreateTuring 
DELETE DeleteTuring

GET LoadTuring
GET auth


User can auth (login logout register)
User can create a turing machine -> Json (or text ?)
User can load a turing machine given a name
User can delete a turing machine



"""

app = fastapi.FastAPI()
app.router = ApiController()
