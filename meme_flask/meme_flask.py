from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        meme_url = data.get("url")
        subreddit = data.get("subreddit")
        return meme_url, subreddit
    except requests.RequestException as e:
        print(f"Error fetching meme: {e}")
        return None, None

@app.route("/")
def index():
    meme_url, subreddit = get_meme()
    context = {
        'meme_url': meme_url,
        "subreddit": subreddit
    }
    return render_template("meme_index.html", **context)

if __name__ == "__main__":
    app.run()
