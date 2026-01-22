from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from starlette.types import Scope, Receive, Send
from fastapi.middleware.gzip import GZipMiddleware
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

# ➤ NEW IMPORT: Profile Router
from API_routes.profile import router as profile_router 

from Database.models import create_tables
from init_schools import initialize_schools
# Initialize DB
initialize_schools()
create_tables()
app = FastAPI()

# Session Middleware (Required for Login & Profile)
app.add_middleware(GZipMiddleware,minimum_size=1000)
app.add_middleware(SessionMiddleware, secret_key="our_secret_key", same_site="lax", https_only=False)

# Static Files
class CachedStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope):
        response = await super().get_response(path, scope)
        # Cache for 1 day (86400 seconds)
        response.headers["Cache-Control"] = "public, max-age=86400"
        return response
app.mount("/static", CachedStaticFiles(directory="static"), name="static")

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

# ➤ CONNECT PROFILE ROUTER
app.include_router(profile_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)