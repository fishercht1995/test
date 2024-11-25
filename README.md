# test

nohup ./s3_download.sh 1 10 0 deploy &> ~/output.log &
nohup ./s3_download.sh 2 10 0 paligemma-3b-mix-224 &> ~/output.log &
nohup ./s3_download.sh 3 10 0 Qwen2-VL-7B-Instruct &> ~/output.log &

nohup ./s3_download.sh 4 10 0 llava-v1.6-mistral-7b-hf &> ~/output.log &
nohup ./s3_download.sh 5 10 0 llava-v1.6-mistral-7b-hf &> ~/output.log &
nohup ./s3_download.sh 6 10 0 llava-v1.6-mistral-7b-hf &> ~/output.log &
nohup ./s3_download.sh 7 10 0 llava-v1.6-mistral-7b-hf &> ~/output.log &

nohup ./s3_download.sh deplot 100 0 &> ~/output.log &
nohup ./s3_download.sh llava-v1.6-mistral-7b-hf 100 0 &> ~/output.log &
nohup ./s3_download.sh llava-v1.6-mistral-7b-hf 100 0 &> ~/output.log &