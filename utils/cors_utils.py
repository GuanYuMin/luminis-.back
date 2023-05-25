from fastapi.middleware.cors import CORSMiddleware

# The domains that will be initially allowed will be placed
# In this case any domain will be allowed

origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
]