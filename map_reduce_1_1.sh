cp /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar .
./start-hadoop.sh
start-hbase.sh
hbase-daemon.sh start thrift
hdfs dfs -mkdir -p input
hdfs dfs -put dataw_fro03.csv input
hdfs dfs -rm -r output_mapreduce_1_1
hadoop jar hadoop-streaming-2.7.2.jar -file mapper_1_1.py -mapper "python3 mapper_1_1.py" -file reducer_1_1.py -reducer "python3 reducer_1_1.py" -input input/dataw_fro03.csv -output output_map_reduce_1_1
