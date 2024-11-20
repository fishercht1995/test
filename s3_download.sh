#!/bin/bash
# 检查参数数量是否小于3
if [ "$#" -lt 3 ]; then
    echo "Error: This script requires at least 3 parameters."
    echo "Usage: $0 param1 param2 param3 [other_params...]"
    exit 1
fi

echo "Model source: $1"
echo "Frequency: $2"
echo "Time interval: $3"

modelnum=$1
# 设置你的 S3 存储桶名称和本地下载目录
BUCKET_NAME="west1model$1"

# 获取所有文件夹的列表
folder="s3://$BUCKET_NAME/"
echo $folder

tshark -i enX0 -f "tcp" -Y "ssl.record.content_type == 23" -w output.pcap &
TSHARK_PID=$!  # 保存 tshark 进程的 PID
echo "PID: $TSHARK_PID"
echo "Tshark is running in the background with PID: $TSHARK_PID"

# 在这里编写脚本的其他逻辑
echo "Script is now running..."
sleep 10  # 模拟脚本运行的其他任务

# 停止 tshark 进程
echo "Stopping Tshark..."
kill "$TSHARK_PID"
echo "Tshark has been stopped."

# 脚本结束
echo "Script finished."