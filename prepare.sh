sudo apt update -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
sudo apt install git-lfs -y
git lfs install
sudo apt install python3-pip -y
sudo apt install python3.12-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip install transformers
pip install accelerate bitsandbytes
pip install torchvision qwen-vl-utils
pip install qwen-vl-utils
pip install huggingface_hub
sudo apt install wireshark tshark -y