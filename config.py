class Config:
    SECRET_KEY = 'your_secret_key'
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB maximum file size

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configurations if needed

def get_config(environment='development'):
    """
    Get the appropriate configuration based on the specified environment.

    :param environment: The environment ('development', 'production', etc.)
    :return: Config object
    """
    if environment == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()
