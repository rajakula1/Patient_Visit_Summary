import whisper

model = whisper.load_model("base")
# result = model.transcribe("/content/drive/MyDrive/MP3/Free_Test_Data_1MB_MP3.mp3")
result = model.transcribe("/content/drive/MyDrive/MP3/sample-0.mp3")
print(result["text"])

from langchain import OpenAI, LLMChain
from langchain_community.llms import OpenAI as LangChainOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

Open_API_Key = open("/content/drive/MyDrive/OpenAI/OpenAI_API_Key.txt", "r")
Open_Api_Key = Open_API_Key.read()
Open_API_Key.close()

llm = OpenAI(model_name="text-davinci-004", openai_api_key=Open_Api_Key, temperature=0)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0, separators=["", ",", "\n"]
)

texts = text_splitter.split_text(result["text"])
print(texts)

docs = text_splitter.create_documents(texts)
print(docs)
chain = load_summarize_chain(llm, chain_type="map_reduce")

output_summaries = chain.run(docs)
print(output_summaries)
