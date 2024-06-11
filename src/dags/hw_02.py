from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner': 'dggz1',
    'start_date': days_ago(1),
}

with DAG(dag_id='02-hw', schedule_interval='@monthly', default_args=default_args) as dag:
    start = DummyOperator(task_id='start', dag=dag)
    stop_task = DummyOperator(task_id='stop_task', dag=dag)
    t1 = DummyOperator(task_id='t1', dag=dag)
    t2_1 = DummyOperator(task_id='t2_1', dag=dag)
    t2_2 = DummyOperator(task_id='t2_2', dag=dag)
    t2_3 = DummyOperator(task_id='t2_3', dag=dag)
    t3_1 = DummyOperator(task_id='t3_1', dag=dag)
    t3_2 = DummyOperator(task_id='t3_2', dag=dag)
    t3_3 = DummyOperator(task_id='t3_3', dag=dag)
    t4 = DummyOperator(task_id='t4', dag=dag)
    end = DummyOperator(task_id='end', dag=dag)

    start >> [stop_task, t1]
    t1 >> [t2_1, t2_2, t2_3]
    t2_1 >> t3_1
    t2_2 >> t3_2
    t2_3 >> t3_3
    [t3_1, t3_2, t3_3] >> t4 >> end
