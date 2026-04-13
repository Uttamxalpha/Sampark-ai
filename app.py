from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert copywriter and content strategist.
Your job:
- Write high-converting content
- Be clear, concise, and persuasive
- Adapt tone based on user input
- Avoid fluff and generic lines
Always:
- Start with a strong hook
- Keep it structured
- End with a clear call-to-action (CTA)
"""),
    ("human", """
Task: {task_type}
Topic/Product: {topic}
Target Audience: {audience}
Tone: {tone}
Extra Instructions: {extra}
Generate high-quality content.
""")
])

api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    temperature=0.7
)

def create_writer_chain():
    parser = StrOutputParser()
    return writer_prompt | model | parser

def run_writer(chain, task_type, topic, audience, tone, extra=""):
    return chain.invoke({
        "task_type": task_type,
        "topic": topic,
        "audience": audience,
        "tone": tone,
        "extra": extra
    })

if __name__ == "__main__":
    print("Writer AI Started\n")

    writer_chain = create_writer_chain()

    print("Enter task: ", end="", flush=True)
    task = input()

    print("Enter topic: ", end="", flush=True)
    topic = input()

    print("Enter audience: ", end="", flush=True)
    audience = input()

    print("Enter tone: ", end="", flush=True)
    tone = input()

    print("Extra instructions: ", end="", flush=True)
    extra = input()

    print("\nGenerating content...\n")

    response = run_writer(
        writer_chain,
        task,
        topic,
        audience,
        tone,
        extra
    )

    print("Generated Content:\n")
    print(response)