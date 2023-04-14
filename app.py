import re

from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"
model = "text-davinci-002"  # change the model as needed

def get_plant_details(plant_name):
    prompt = f"Generate details for the plant {plant_name}:\n\nScientific name:\nFlower type:\nSeed types:\nSeason type:\nPreferred soil type:\nPreferred pH level:\nPreferred nutrition:\nHarvest time:\nPlant compatibility:"
    model = "text-davinci-002" # change the model as needed
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    if response.choices[0].text:
        return response.choices[0].text
    else:
        return "Plant not found."




@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        plant_name = request.form.get("plant_name")
        plant_details = get_plant_details(plant_name)
        return render_template("results.html", plant_name=plant_name, plant_details=plant_details)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
