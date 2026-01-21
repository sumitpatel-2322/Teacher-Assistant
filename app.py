from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

# Import Routers
from API_routes.voice import router as voice_router
from API_routes.dashboard import router as dashboard_router
from API_routes.home import router as home_router
from API_routes.login import router as login_router
from API_routes.teacher_dashboard import router as teacher_router
from API_routes.register import router as register_router
from API_routes.arp import router as arp_router
from API_routes.crp import router as crp_router
from API_routes.brp import router as brp_router
from API_routes.registered import router as registered_router
from API_routes.solution_details import router as solution_details_router
from API_routes.micro import router as micro_router
from API_routes.micro_add import router as micro_add_router
from API_routes.community import router as community_router


# ➤ NEW IMPORT
from API_routes.profile import router as profile_router 

from Database.models import create_tables

# Initialize DB
create_tables()

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="our_secret_key", same_site="lax", https_only=False)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Include Routers
app.include_router(voice_router)
app.include_router(home_router)
app.include_router(login_router)
app.include_router(register_router)
app.include_router(registered_router)
app.include_router(dashboard_router)
app.include_router(teacher_router)
app.include_router(solution_details_router)
app.include_router(arp_router)
app.include_router(crp_router)
app.include_router(brp_router)
app.include_router(micro_router)
app.include_router(micro_add_router)
app.include_router(community_router)  

# ➤ INCLUDE PROFILE ROUTER
app.include_router(profile_router)