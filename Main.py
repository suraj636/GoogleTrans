from fastapi import FastAPI, HTTPException
from googletrans import Translator

# Initialize FastAPI app
app = FastAPI()

# Initialize the translator
translator = Translator()

# Define the endpoint
@app.post("/translate/")
async def translate_text(sentence: str, lang_code: str):
    try:
        # Translate the sentence
        translation = translator.translate(sentence, dest=lang_code)
        return {
            "original_text": sentence,
            "translated_text": translation.text,
            "source_language": translation.src,
            "destination_language": translation.dest,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)