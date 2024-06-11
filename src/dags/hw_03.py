import datetime as dt
import json

from airflow.models import DAG
from airflow.operators.python import PythonOperator, get_current_context
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

default_args = {
    'owner': 'dggz1',
    'start_date': dt.datetime(2024, 6, 1),
}


def odd_only():
    context = get_current_context()
    execution_date = context['execution_date']

    if execution_date.day % 2 == 0:
        raise ValueError(f'Even day: {execution_date}')


with DAG(dag_id='03-hw',
         schedule_interval='@hourly',
         default_args=default_args) as dag:

    odd_only_task = PythonOperator(
        task_id='odd_only',
        python_callable=odd_only,
        dag=dag,
    )

    http_request = SimpleHttpOperator(
        task_id="http_request",
        http_conn_id="dog_facts_conn_id",
        method="GET",
        endpoint="/facts",
        response_filter=lambda resp: json.loads(resp.text)['facts'][0],
        do_xcom_push=True,
        dag=dag,
    )

    sleep_echo = BashOperator(
        task_id="sleep_and_echo",
        bash_command="sleep 1; echo {{ ti.xcom_pull(task_ids='http_request') }}",
        dag=dag,
    )

    odd_only_task >> http_request >> sleep_echo
