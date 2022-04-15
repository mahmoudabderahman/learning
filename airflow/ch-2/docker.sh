winpty docker run \
-ti \
-p 8080:8080 \                                                             
-v  /dag.py:/opt/airflow/dags/          
    dag.py \                                          
--entrypoint=/bin/bash \
--name airflow \
apache/airflow:2.0.0-python3.8 \                                           
-c '( \
airflow db init && \                                                       
 airflow users create --username admin --password admin --firstname      
    Anonymous --lastname Admin --role Admin --email admin@example.org \    
); \
airflow webserver & \                                                      
airflow scheduler \                                                        
'