from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-04-17T08:42:00', 'schedule': '@once', 'catchup': False, 'dag_id': '6c1676e443cc4840ab1d726543fa40e1'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    DockerExcu_b82a4282005f455f86bcd3a8ad4c9d9a = Task(
        dag,
        task_id='DockerExcu_b82a4282005f455f86bcd3a8ad4c9d9a',
        workspace_id=4,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'DockerExcuteSegmentedUploadPiece', 'source_image': 'ghcr.io/mockingbird1234/trusted_data_custom_domino_pieces:development-group0', 'repository_url': 'https://github.com/Mockingbird1234/trusted_data_custom_domino_pieces', 'repository_version': 'development'},
        piece_input_kwargs={'piece_cus_name': 'ces', 'supplement_command': 'pwd\nls', 'working_directory': '/tmp/', 'has_output': False}
    )()

