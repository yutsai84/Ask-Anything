import os

from langchain.agents.initialize import initialize_agent
from langchain.agents.tools import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms.openai import OpenAI
from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI
import re
import gradio as gr
import openai

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_KEY"] = os.environ[
    "AZURE_OPENAI_NONREDUNDANT_ACCESS_KEY_DEVELOPMENT"
]

os.environ["OPENAI_API_BASE"] = os.environ[
    "AZURE_OPENAI_NONREDUNDANT_ENDPOINT_DEVELOPMENT"
]
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"


GPT4 = AzureChatOpenAI(
    deployment_name="gpt-4-32k",
    model_name="gpt4-32k",
    openai_api_base=os.environ["OPENAI_API_BASE"],
    openai_api_version="2023-03-15-preview",
    temperature=0,
    model_kwargs={"top_p": 0.01},
)


class ConversationBot:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", output_key='output')
        self.tools = []

    def run_text(self, text, state):
        res = self.agent({"input": text.strip()})
        res['output'] = res['output'].replace("\\", "/")
        response = res['output'] 
        state = state + [(text, response)]
        print(f"\nProcessed run_text, Input text: {text}\nCurrent state: {state}\n"
              f"Current Memory: {self.agent.memory.buffer}")
        return state, state


    def init_agent(self, image_caption, dense_caption, video_caption, tags, state):
        chat_history =''
        PREFIX = "ChatVideo is a chatbot that chats with you based on video descriptions."
        FORMAT_INSTRUCTIONS = """
        When you have a response to say to the Human,  you MUST use the format:
        ```
        {ai_prefix}: [your response here]
        ```
        """
        SUFFIX = f"""You are a chatbot that conducts conversations based on video descriptions. You mainly answer based on the given description, and you can also modify the content according to the tag information, and you can also answer the relevant knowledge of the person or object contained in the video. The second description is a description for one second, so that you can convert it into time. When describing, please mainly refer to the sceond description. Dense caption is to give content every five seconds, you can disambiguate them in timing. But you don't create a video plot out of nothing.

                Begin!

                Video tags are: {tags}

                The second description of the video is: {image_caption}

                The dense caption of the video is: {dense_caption}

                The general description of the video is: {video_caption}"""+"""Previous conversation history {chat_history}

                New input: {input}

                {agent_scratchpad}
                """
        self.memory.clear()
        self.llm = GPT4
        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent="conversational-react-description",
            verbose=True,
            memory=self.memory,
            return_intermediate_steps=True,
            agent_kwargs={'prefix': PREFIX, 'format_instructions': FORMAT_INSTRUCTIONS, 'suffix': SUFFIX}, )
        state = state + [("I upload a video, Please watch it first! ","I have watch this video, Let's chat!")]
        return gr.update(visible = True),state, state,
if __name__=="__main__":
    import pdb
    pdb.set_trace()
