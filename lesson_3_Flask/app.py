from flask import Flask, render_template
import uuid
import time
import datetime


app = Flask(__name__)


@app.route('/get_data/<number_of_lines>')
def homepage(number_of_lines=1):
    output_list = []
    for i in range(int(number_of_lines)):
        start = time.monotonic()
        uuid_info = uuid.uuid4()
        local_time = datetime.datetime.now()
        local_time = local_time.strftime("%d-%m-%Y %H:%M:%S")
        end = time.monotonic()
        duration = end - start
        output_list.append({})
        output_list[i]["uuid_info"] = uuid_info
        output_list[i]["local_time"] = local_time
        output_list[i]["duration"] = duration
    return render_template("index.html", number_of_lines=int(number_of_lines),  output_list=output_list)


if __name__ == "__main__":
    app.run(debug=True)
