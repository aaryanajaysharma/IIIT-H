#/bin/bash
printf "Running runner_script.sh\n"

chmod +x mapper0.py
chmod +x reducer0.py
chmod +x mapper1.py
chmod +x reducer1.py

HADOOP_JAR="$1"
INPUT_FOLDER="$2"
HDFS_INPUT_FOLDER="$3"
HDFS_OUTPUT_FOLDER="$4"

hdfs dfs -rm -r "$HDFS_INPUT_FOLDER"

if ! hadoop fs -test -d "$HDFS_INPUT_FOLDER"; then
    printf "Creating HDFS_INPUT_FOLDER: $HDFS_INPUT_FOLDER"
    hadoop fs -mkdir -p "$HDFS_INPUT_FOLDER"
fi
# Copy all files from INPUT_FOLDER to HDFS_INPUT_FOLDER
printf "Copying files from $INPUT_FOLDER to $HDFS_INPUT_FOLDER"
hadoop fs -copyFromLocal "$INPUT_FOLDER"/* "$HDFS_INPUT_FOLDER"
hdfs dfs -rm -r "$HDFS_OUTPUT_FOLDER"
hdfs dfs -rm -r "${HDFS_OUTPUT_FOLDER}0"

printf "Running mapper0 and reducer0\n"
mapred streaming -files mapper0.py,reducer0.py -input "$HDFS_INPUT_FOLDER/*" -output "${HDFS_OUTPUT_FOLDER}0" -mapper mapper0.py -reducer reducer0.py -numReduceTasks 3
printf "Running mapper1 and reducer1\n"
mapred streaming -files mapper1.py,reducer1.py -input "${HDFS_OUTPUT_FOLDER}0/part-0000*" -output "$HDFS_OUTPUT_FOLDER" -mapper mapper1.py -reducer reducer1.py -numReduceTasks 3
printf "finished running runner_script.sh\n"
printf "Output:\n"
hdfs dfs -cat "$HDFS_OUTPUT_FOLDER/part-0000*" | sort