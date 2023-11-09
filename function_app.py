import azure.functions as func
import logging, requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpTrigger")
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    
    if req_body:
        logging.info(f'Req Body: {req_body}')
        requests.post(url='https://webhook.site/912436ea-f2b4-4836-9086-9cfef7259a3f', json=req_body)

        return func.HttpResponse("Solicitação processada.",  status_code=200)
    else:
        return func.HttpResponse("Sintaxe de solicitação malformada.", status_code=400)