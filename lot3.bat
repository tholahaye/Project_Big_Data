docker cp lot3_1.sh hadoop-master:/root/
docker cp lot3_2.sh hadoop-master:/root/
docker exec hadoop-slave1 /bin/bash -c './service_slv.sh'
docker exec hadoop-slave2 /bin/bash -c './service_slv.sh'
docker exec hadoop-master /bin/bash -c './lot3_1.sh'
python lot3.py dataw_fro03.csv
docker exec hadoop-master /bin/bash -c './lot3_2.sh'