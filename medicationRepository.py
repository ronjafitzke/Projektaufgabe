from shared import db
from models import Medication, Prescription

class MedicationRepository:
    @staticmethod
    def get_all_medications(): # Holt alle Medikamente aus der Datenbank
        return Medication.query.all()

    @staticmethod
    def get_medication_by_id(medication_id): # Holt ein Medikament anhand seiner ID aus der Datenbank
        return Medication.query.get(medication_id)

    @staticmethod
    def add_medication(name, dosage): # fügt ein neues Medikament zur Datenbank hinzu.
        medication = Medication(name=name, dosage=dosage)
        db.session.add(medication)
        db.session.commit()

    @staticmethod
    def update_medication(medication_id, name, dosage): # Aktualisiert ein vorhandenes Medikament in der Datenbank
        medication = Medication.query.get(medication_id)
        if medication:
            medication.name = name
            medication.dosage = dosage
            db.session.commit()

    @staticmethod
    def delete_medication(medication_id): # Löscht ein Medikament aus der Datenbank.
        medication = Medication.query.get(medication_id)
        if medication:
            db.session.delete(medication)
            db.session.commit()

    # We can add more methods as needed for medication management

    @staticmethod
    def add_prescription(medication_id, patient_name, date): # Fügt eine neue Verschreibung für ein Medikament hinzu.
        prescription = Prescription(medication_id=medication_id, patient_name=patient_name, date=date)
        db.session.add(prescription)
        db.session.commit()