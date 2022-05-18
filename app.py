from flask import Flask, Response, request
import json
from db import users


def create_app():
    app = Flask(__name__)

    @app.get("/api/v1.0/users")
    def get_users():
        return Response(json.dumps(users), 200, content_type="application/json")

    @app.post("/api/v1.0/users")
    def post_users():
        user = request.json
        users.append(user)
        return Response(json.dumps(user), 201, content_type="application/json")

    return app


if __name__ == "__main__":
    create_app().run()