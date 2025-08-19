import subprocess


def summarize_text(text: str) -> str:
    """
    Summarize the given text using the local Ollama Mistral model.

    Args:
        text (str): Transcript text to summarize.

    Returns:
        str: Summarized text or error message if summarization fails.
    """
    if not text.strip():
        return "No transcript available to summarize."

    # Limit text length to avoid overloading the model
    prompt = f"Summarize this YouTube transcript in 5 bullet points:\n\n{text[:4000]}"

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),
            capture_output=True,
            check=True
        )
        return result.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode("utf-8") if e.stderr else str(e)
        return f"Error running summarizer: {error_msg}"
    except FileNotFoundError:
        return "Ollama executable not found. Make sure Ollama is installed and in your PATH."
