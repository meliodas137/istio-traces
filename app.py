from opentelemetry import trace
from opentelemetry import metrics

from random import randint
from flask import Flask, request

tracer = trace.get_tracer(__name__)
meter = metrics.get_meter(__name__)

roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)

app = Flask(__name__)

@app.route("/rolldice")
def roll_dice():
    return str(do_roll())

def do_roll():
    with tracer.start_as_current_span("do_roll") as rollspan:  
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": res})
        return res

# if __name__ == '__main__':
#     # app.run(host="0.0.0.0:5050")
#     app.run(debug=True)
    
# docker run -p 4317:4317 -v "C:/Users/mayan/Desktop/Git Repo/Sem 2/Big data & ML/tmp/otel-collector-config.yaml":"/etc/otel-collector-config.yaml" otel/opentelemetry-collector:latest --config="/etc/otel-collector-config.yaml"

    