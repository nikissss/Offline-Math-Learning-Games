from fastapi import FastAPI, HTTPException
from transcript import fetch_transcript
from summarizer import summarize_text

app = FastAPI(title="YouTube Transcript Summarizer", version="1.0")


@app.get("/")
def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "YouTube Transcript Summarizer API is running"}


@app.get("/summarize/{video_id}")
def summarize(video_id: str):
    """
    Fetch transcript for a given YouTube video ID and return summarized text.

    Args:
        video_id (str): YouTube video identifier.

    Returns:
        dict: JSON with video_id and summarized text.
    """
    try:
        transcript_text = fetch_transcript(video_id)
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

    summary = summarize_text(transcript_text)
    return {"video_id": video_id, "summary": summary}
