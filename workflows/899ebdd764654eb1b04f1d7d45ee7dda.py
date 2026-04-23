from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-04-23T06:14:00', 'schedule': '@once', 'catchup': False, 'dag_id': '899ebdd764654eb1b04f1d7d45ee7dda'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_27dd10b0cd4b41a5bb118468b0a3c60b = Task(
        dag,
        task_id='HttpReques_27dd10b0cd4b41a5bb118468b0a3c60b',
        workspace_id=5,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'url': 'https://tse3.mm.bing.net/th/id/OIP.XV-mvuX9EN2Pn0BZvhdf1gHaEK?rs=1&pid=ImgDetMain&o=7&rm=3', 'method': 'GET', 'bearer_token': None, 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()
    ImageFilte_7a0d7be2528e4149831ad0a4308dcb62 = Task(
        dag,
        task_id='ImageFilte_7a0d7be2528e4149831ad0a4308dcb62',
        workspace_id=5,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_27dd10b0cd4b41a5bb118468b0a3c60b', 'output_arg': 'base64_bytes_data'}, 'sepia': False, 'black_and_white': True, 'brightness': False, 'darkness': False, 'contrast': False, 'red': False, 'green': False, 'blue': False, 'cool': True, 'warm': False, 'output_type': 'both'}
    )()

    ImageFilte_7a0d7be2528e4149831ad0a4308dcb62.set_upstream([globals()[t] for t in ['HttpReques_27dd10b0cd4b41a5bb118468b0a3c60b']])
