from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse
from fastapi import Request
#para poder usar el token
from auth.authentication import validate_token


class AccessRouteForTokenMiddleware(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def access_route_for_token(request: Request):
            if "Authorization" not in request.headers:
                return JSONResponse(status_code=401, content={"message": "Token not found"})
            token = request.headers["Authorization"].split(" ")[1]
            validate = validate_token(token, output=False)
            if validate == None:
                return await original_route(request)
            else:
                return validate
            
        return access_route_for_token