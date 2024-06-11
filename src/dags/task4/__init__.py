from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from .operator import BrawlStatsOperator

BS_PLAYER_TAG = Variable.get("BS_PLAYER_TAG")

with DAG(
        dag_id='04-hw-bs',
        start_date=datetime(2024, 6, 1),
        schedule_interval='@weekly',
        max_active_runs=3,
        default_args={'owner': 'dggz1'}
) as dag:
    get_trophies = BrawlStatsOperator(
        task_id='get_trophies',
        player_tag=BS_PLAYER_TAG,
        dag=dag
    )
