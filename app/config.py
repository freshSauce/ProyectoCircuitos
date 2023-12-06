import os

SECRET_KEY = os.getenv("SECRET_KEY")
# Resto de tus configuraciones...


class Config:
    # Configuraciones generales de la aplicación Flask

    # Clave secreta para proteger las sesiones y cookies
    SECRET_KEY = SECRET_KEY


class DevelopmentConfig(Config):
    # Configuraciones específicas para el entorno de desarrollo

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

class ProductionConfig(Config):
    # Configuraciones específicas para el entorno de producción

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Configuración de la aplicación Flask
app_config = {"development": DevelopmentConfig, "production": ProductionConfig}
