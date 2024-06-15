from flask import render_template
from shared import app
from medicationRepository import MedicationRepository


@app.route('/')
def home():
    medications = MedicationRepository.get_all_medications()
    return render_template('home.html', medications=medications)