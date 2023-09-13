# Sage Foundation Hackathon Project: Automating Parent-Child Interaction (PCI) Analysis

**Project Description:**
In order to support [Dr.Addyman's team's](https://github.com/InfantLab/VASC) pursuit to advance public health solutions, this project uses Multimodal LLMs to delve into parent-child dynamics.

This project leverages the work from [Ask-Anything](https://github.com/OpenGVLab/Ask-Anything/tree/main/video_chat_with_ChatGPT).

**Mission:**
We're on a quest to:
1. Craft a solution to gauge how parents connect with their babies.
2. Extract metrics between parent and infant from video recordings.

**Significance:**
Harnessing this technology can streamline the allocation of essential health services, prioritizing areas with the most need. This is pivotal for regions in the Global South grappling with resource constraints.


# VideoChat

VideoChat is a multifunctional video question answering tool that combines the functions of Action Recognition, Visual Captioning and ChatGPT. Our solution generates dense, descriptive captions for any object and action in a video, offering a range of language styles to suit different user preferences. It supports users to have conversations in different lengths, emotions, authenticity of language.
- Video-Text Generation
- Chat about uploaded video
- Interactive demo

# :fire: Updates

- **2023/04/19**: Code Release

# :speech_balloon: Example

![images](assert/hugging.png)
![images](assert/dancing.png)
![images](assert/dancing2.png)

# :running: Usage

```shell
# We recommend using conda to manage the environment and use python3.8.16  
conda create -n chatvideo python=3.8.16  
conda activate chatvideo  

# Install system dependencies

conda install -c "nvidia/label/cuda-11.7.0" cuda-toolkit
conda install "gxx[version=">=6,<11.5.0"]"
conda install -c fastai opencv-python-headless
conda install -c conda-forge git-lfs
conda install -c conda-forge ninja

  
# Clone the repository:  
git clone https://github.com/OpenGVLab/Ask-Anything.git  
cd ask-anything/video_chat_with_ChatGPT
  
# Install dependencies:  
pip install -r requirements.txt  
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz  
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'  
  
# Download the checkpoints  
mkdir pretrained_models  
wget -P ./pretrained_models https://huggingface.co/spaces/xinyu1205/Tag2Text/resolve/main/tag2text_swin_14m.pth  
wget -P ./pretrained_models https://datarelease.blob.core.windows.net/grit/models/grit_b_densecap_objectdet.pth  
git clone https://huggingface.co/mrm8488/flan-t5-large-finetuned-openai-summarize_from_feedback ./pretrained_models/flan-t5-large-finetuned-openai-summarize_from_feedback  
cd ./pretrained_models/flan-t5-large-finetuned-openai-summarize_from_feedback  
git lfs pull  
cd ../..  
  
# Note: we use AzureOpenAI instead
# Configure the necessary ChatGPT APIs  
# export OPENAI_API_KEY={Your_Private_Openai_Key}
  
# Run the VideoChat gradio demo.  
python app.py  
```

# Acknowledgement

The project is based on [InternVideo](https://github.com/OpenGVLab/InternVideo), [Tag2Text](https://github.com/xinyu1205/Tag2Text), [GRiT](https://github.com/JialianW/GRiT), [mrm8488](https://huggingface.co/mrm8488/flan-t5-large-finetuned-openai-summarize_from_feedback) and [ChatGPT](https://openai.com/blog/chatgpt). Thanks for the authors for their efforts.

