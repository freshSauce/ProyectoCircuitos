import os

SECRET_KEY = os.getenv("SECRET_KEY")
# Resto de tus configuraciones...


class Config:
    # Configuraciones generales de la aplicación Flask

    # Clave secreta para proteger las sesiones y cookies
    SECRET_KEY = SECRET_KEY

    # Resto de tus configuraciones...


class DevelopmentConfig(Config):
    # Configuraciones específicas para el entorno de desarrollo

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    # Resto de tus configuraciones de desarrollo...


class ProductionConfig(Config):
    # Configuraciones específicas para el entorno de producción

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    # Resto de tus configuraciones de producción...


# Configuración de la aplicación Flask
app_config = {"development": DevelopmentConfig, "production": ProductionConfig}
