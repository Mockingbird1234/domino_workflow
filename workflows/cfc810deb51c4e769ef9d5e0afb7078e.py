from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-04-17T08:35:00', 'schedule': '@once', 'catchup': False, 'dag_id': 'cfc810deb51c4e769ef9d5e0afb7078e'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_fa412491ce3c486d95c34d2cc8faa0a4 = Task(
        dag,
        task_id='HttpReques_fa412491ce3c486d95c34d2cc8faa0a4',
        workspace_id=3,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'method': 'GET', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()

