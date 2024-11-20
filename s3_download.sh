#!/bin/bash

if [ "$#" -lt 3 ]; then
    echo "Error: This script requires at least 3 parameters."
    echo "Usage: $0 param1 param2 param3 [other_params...]"
    exit 1
fi
mkdir ~/out
echo "Model source: $1"
echo "Frequency: $2"
echo "Time interval: $3"

modelnum=$1
# 设置你的 S3 存储桶名称和本地下载目录
BUCKET_NAME="west1model$1"


folder="s3://$BUCKET_NAME/llava-v1.6-mistral-7b-hf"
echo $folder

#sudo tshark -i enX0 -f "tcp" -Y "ssl.record.content_type == 23" -w ~/output.pcap &
#sudo sudo tshark -i enX0 -f "tcp port 443" -w /tmp/output.pcap &
sudo tshark -i enX0 -f "tcp port 443 and tcp[13] & 0x02 != 0" -w /tmp/output.pcap &
TSHARK_PID=$!  # 保存 tshark 进程的 PID
echo "PID: $TSHARK_PID"
echo "Tshark is running in the background with PID: $TSHARK_PID"


for i in $(seq 1 $2); do
    echo "Start download：$folder Freq: $i"

    # 记录开始时间
    start_time=$(date +"%Y-%m-%d %H:%M:%S")

    # 下载文件夹
    aws s3 cp $folder ./temp --recursive

    # 记录完成时间
    end_time=$(date +"%Y-%m-%d %H:%M:%S")

    # 计算下载时间
    start_seconds=$(date -d "$start_time" +%s)
    end_seconds=$(date -d "$end_time" +%s)
    download_time=$((end_seconds - start_seconds))

    echo "$2;$i;$3;$download_time" >> ~/download_time

    # 删除已下载的文件夹
    rm -rf temp
    echo "--------------------------"
    sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
    sleep $3
done 

echo "Stopping Tshark..."
kill "$TSHARK_PID"
echo "Tshark has been stopped."
sudo mv /tmp/*.pcap ~/out/
# 脚本结束
echo "Script finished."
