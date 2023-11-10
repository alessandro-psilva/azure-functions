import azure.functions as func
import uuid
import os
import json
import requests
import logging

bp = func.Blueprint()


@bp.function_name(name="hook")
@bp.route(route="hook", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
def hook(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("[hook] HTTP trigger function processed a request.")
    req_body = req.get_json()
    hook = req_body.get("hook", "")

    if hook:
        logging.info(f"Req Body: {req_body}")
        response = requests.post(
            url="https://webhook.site/912436ea-f2b4-4836-9086-9cfef7259a3f",
            json=req_body,
        )

        return func.HttpResponse(
            json.dumps({"ResponseHook": response.text}), status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"RequestHook": "Input Null"}), status_code=400
        )
