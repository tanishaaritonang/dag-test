from datetime import datetime
from airflow.sdk import dag, task


@dag(
    dag_id="hello_world",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["demo"],
)
def hello_world():

    @task
    def say_hello():
        print("Hello from Airflow")

    say_hello()


hello_world()