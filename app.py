import time
from predictor import predict_failure

print("System Failure Predictor Started...\n")

while True:
    result = predict_failure()
    print(result)
    time.sleep(5)
