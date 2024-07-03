import os
from fastapi.responses import JSONResponse
from app.common.errors import errors
from io import StringIO
from configparser import ConfigParser


def custom_exception_handler(req, exc):
    """ Custom exception handler
    :param req - Request object
    :param exc - Exception

    :returns - Define error message for custom exception
    """

    # req.app.logger.info(f"Custom Exception {exc.__class__.__name__} on {req.url.path}")
    return JSONResponse(content=errors.get(exc.__class__.__name__, errors['Exception']),
                        status_code=errors.get(exc.__class__.__name__, errors['Exception'])['status'])


def read_properties_file(file_path):
    with open(file_path) as f:
        config = StringIO()
        config.write('[dummy_section]\n')
        config.write(f.read().replace('%', '%%'))
        config.seek(0, os.SEEK_SET)
        cp = ConfigParser()
        cp.read_file(config)
        return dict(cp.items('dummy_section'))
