import requests

elasticsearch_url = 'https://localhost:9200'
pipeline = "SystemLogs"
username = "elastic"
password = "v=Vopwf2SSiA6KMGkT78"

log_file_path = "/var/log/syslog"

def process_logs(log_file_path):
    with open(log_file_path, "r") as logfile:
        for line in logfile:
            payload = {
                "message": line.strip()
            }
            response = requests.post(
                f"{elasticsearch_url}/_ingest/pipeline/{pipeline}/_simulate",
                json={"docs": [{"_source": payload}]},
                auth=(username, password),
                verify=False
            )
            if response.status_code == 200:
                print(f"Successfully ingested: {line.strip()}")
            else:
                print(f"Failed to ingest: {line.strip()} - {response.text}")
            print(response.json())
            
process_logs(log_file_path)