from shared import db

class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Medication {self.name}>'

class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    medication = db.relationship('Medication', backref=db.backref('prescriptions', lazy=True))

    def __repr__(self):
        return f'<Prescription {self.patient_name}>'
