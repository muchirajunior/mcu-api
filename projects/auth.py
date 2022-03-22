from functools import wraps
import sys
sys.path.append("..")
from main import app,request


def authorization(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if "auth" in request.headers:
            token=request.headers["auth"]

            if token != app.config["SECRET_KEY"]:
                return {"msg":"invalid key"},401

        else:
            return {"msg":"missing key"},401

        return f(*args, **kwargs)

    return decorator