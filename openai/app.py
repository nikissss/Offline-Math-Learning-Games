from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Summarization API")

# Initialize Gemini client (OpenAI-compatible)
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


class SummarizeRequest(BaseModel):
    text: str
    max_length: int | None = 200  # optional word limit


@app.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    try:
        # Calling Gemini for summarization
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": "You are a concise and clear summarizer."},
                {"role": "user", "content": f"Summarize the following text in under {request.max_length} words:\n\n{request.text}"}
            ],
            temperature=0.5,
        )

        summary = response.choices[0].message.content.strip()
        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
