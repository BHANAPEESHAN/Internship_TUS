from flask import Flask, render_template, request
import fitz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_content():
    file = request.files['document']
    sentences = []
    # Open the document using fitz
    #doc = fitz.open(stream=file.read(), filetype="pdf")
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            texts = page.get_text("text").split("\n")
        # print(text)
        for text in texts:
                # Splitting the text block into sentences and adding them to the list
                sentences.extend(text.split(". "))
                #print(sentences)
    #extracted_text = ""
    #
    #for page in doc:
    #    extracted_text += page.getText()
    #
    return sentences

if __name__ == '__main__':
    app.run(debug=True)
