import azure.functions as func
from routes.hook.hook import bp as hook

app = func.FunctionApp()

# routes
app.register_functions(hook)
