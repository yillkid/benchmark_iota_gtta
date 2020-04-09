import requests
import json
import matplotlib.pyplot as plt
import numpy as np

HOST_NAME = "node1"
HOST = 'http://localhost:14265'
DEPTH = 4
TEST_TIMES = 100

list_x_axis = []
list_duration = []

def gtta():
    # Http header and parameters
    req_headers = {"content-type": "application/json","X-IOTA-API-Version": "1"}
    req_data = {"command": "getTransactionsToApprove", "depth": DEPTH}

    # POST request
    r = requests.post(HOST, data = json.dumps(req_data), headers = req_headers)

    return r.text

def plot_and_export(list_x_axis, list_duration):
    plt.plot(list_x_axis, list_duration)
    # plt.show()
    plt.savefig(HOST_NAME + '_gtta_benchmark.png', bbox_inches='tight')

for index in range(TEST_TIMES):
    print("Starting GTTA in " + str(index + 1) + "/" + str(TEST_TIMES) + " ... ")
    obj_response = json.loads(gtta())
    
    print("Duration: " + str(obj_response["duration"]))
    list_x_axis.append(str(index))
    list_duration.append(obj_response["duration"])
    
# Plot
print("Starting to plot ...")
plot_and_export(list_x_axis, list_duration)
print("Done")
