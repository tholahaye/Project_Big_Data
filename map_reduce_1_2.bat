docker cp mapper_1_2.py hadoop-master:/root/
docker cp reducer_1_2.py hadoop-master:/root/
docker cp dataw_fro03.csv hadoop-master:/root/
docker cp map_reduce_1_2.sh hadoop-master:/root/
docker exec hadoop-slave1 /bin/bash -c './service_slv.sh'
docker exec hadoop-slave2 /bin/bash -c './service_slv.sh'
docker exec hadoop-master /bin/bash -c './map_reduce_1_2.sh'