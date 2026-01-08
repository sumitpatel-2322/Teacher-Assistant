from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# import sqlite3
from API_routes.home import router as home_router
from API_routes.login import router as login_router
from API_routes.teacher_dashboard import router as teacher_router
from API_routes.register import router as register_router
from API_routes.arp import router as arp_router
from API_routes.crp import router as crp_router
from API_routes.brp import router as brp_router
from API_routes.registered import router as registered_router
from Database.models import create_teacher_table
create_teacher_table()
app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
app.include_router(home_router)
app.include_router(login_router)
app.include_router(teacher_router)
app.include_router(register_router)
app.include_router(arp_router)
app.include_router(crp_router)
app.include_router(brp_router)
app.include_router(registered_router)