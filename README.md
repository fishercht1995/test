# test

nohup ./s3_download.sh 1 10 0 &> ~/output.log &
nohup ./s3_download.sh 2 10 1800 &> ~/output.log &
nohup ./s3_download.sh 3 10 7200 &> ~/output.log &
nohup ./s3_download.sh 4 10 14400 &> ~/output.log &


nohup ./s3_download.sh 1 10 0 deploy &> ~/output.log &
nohup ./s3_download.sh 2 10 0 paligemma-3b-mix-224 &> ~/output.log &
nohup ./s3_download.sh 3 10 0 Qwen2-VL-7B-Instruct &> ~/output.log &
nohup ./s3_download.sh 4 10 0  &> ~/output.log &