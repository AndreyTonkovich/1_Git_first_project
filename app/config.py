import os

HELLO_MESSAGE="Config data load"
SECRET_KEY="hA10sgHaghi>78FF8cDBrtf3dsdaklk>"
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")#, "sqlite:///db/data.db") 
SQLALCHEMY_TRACK_MODIFICATIONS = False
