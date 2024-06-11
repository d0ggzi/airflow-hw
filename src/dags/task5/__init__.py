from datetime import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.models import Variable
from .operator import BrawlStatsOperator

BS_PLAYER_TAG = Variable.get("BS_PLAYER_TAG")
POSTGRES_CONN_ID = 'postgres_hw'

with DAG(
        dag_id='05-hw-bs',
        start_date=datetime(2024, 6, 1),
        schedule_interval='@daily',
        max_active_runs=3,
        default_args={'owner': 'dggz1'}
) as dag:
    create_table = PostgresOperator(
        task_id='create_table_task',
        sql='sql/create_table.sql',
        postgres_conn_id=POSTGRES_CONN_ID,
    )

    get_trophies = BrawlStatsOperator(
        task_id='get_trophies',
        player_tag=BS_PLAYER_TAG,
        dag=dag,
        do_xcom_push=True,
    )

    insert_rate = PostgresOperator(
        task_id='insert_rate',
        postgres_conn_id=POSTGRES_CONN_ID,
        sql='sql/insert_rate.sql',
        params={
            'player_tag': BS_PLAYER_TAG,
        }
    )

    create_table >> get_trophies >> insert_rate
