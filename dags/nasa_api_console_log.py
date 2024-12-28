import datetime
import psycopg2

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable, Connection
from modules.nasa_api.nasa_api import NasaAPI

my_dag = DAG(
    dag_id="nasa_api_console_log",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)

def nasa_api_get_data():
    
    api_key = Variable.get("nasa_api_key")
    if api_key:
        nasa_api = NasaAPI(api_key)
        print(nasa_api.parse_neo_data()["objects"][0])
    else:
        print("No nasa_api_key")


PythonOperator(
    task_id="nasa_api_get_data", dag=my_dag, python_callable=nasa_api_get_data
)
