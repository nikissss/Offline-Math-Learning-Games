from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound


def fetch_transcript(video_id: str) -> str:
    """
    Fetches the transcript text of a YouTube video (auto-generated or manual captions)

    Args:
        video_id (str): The unique YouTube video ID.

    Returns:
        str: Combined transcript text.

    Raises:
        RuntimeError: If transcript is unavailable or an error occurs.
    """
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        # Try to get English transcript
        transcript = transcript_list.find_transcript(['en'])
        # Combine all transcript segments into one string
        text = " ".join([t['text'] for t in transcript.fetch()])
        return text
    except TranscriptsDisabled:
        raise RuntimeError("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise RuntimeError("No transcript found for this video.")
    except Exception as e:
        raise RuntimeError(f"Error fetching transcript: {e}")
