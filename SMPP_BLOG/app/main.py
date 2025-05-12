from flask import FLASK, request, jsonify
from stregatto import Stregatto
from regolo_plugin.rules import format_blog_post
import openai
import os

app = Flask(__name__)
stregatto = Stregatto()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate',
           methods=['POST'])
def generate_article():
    data = request.get_json()
    prompt = data.get('prompt', "")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    raw_content = response.choices[0].text.strip()

    formatted_content = format_blog_post(raw_content)

    return jsonify({'article':formatted_content})

    if _name_ == '__main__':
        app.run(host='0.0.0.0', port=8000)