## Data pipeline. Brazilian E-Commerce Public Dataset by Olist
### About
    This is my simple data pipeline as a pet project. Pipeline load some .csv files from kaggle.com using Airflow, 
    Postgres and show some metrics in BI-instrument Superset.
    
    https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data?select=olist_products_dataset.csv

## Quick start
1. Go to folder 
```cmd
cd de_pipeline
```

2. Create linked folders to airflow container
```cmd
mkdir -p ./dags ./logs ./plugins ./config
```

3. Run and bould image
```cmd 
docker compose up
```

4. Await full installation and go to http://localhost:8080/login/

5. Login with
    - username: airflow
    - password: airflow
  
6. Now you can see the `simple_dag` in list of dags in the first page. It is the marker that all works good for now.

7. To stop docker-compose run
```cmd
docker-compose down
```