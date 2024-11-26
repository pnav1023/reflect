from openai import OpenAI
import os
from dotenv import load_dotenv


def get_question(entries):
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", 
            "content": f"""
            Give me 3 questions a therapist might ask and make it personalized based on the following info.

            journal entries: {entries}
            """}
        ]
    )

    return completion.choices[0].message.content
