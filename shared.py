from flask import Flask # Flask wird importiert, um die Flask-Anwendung zu erstellen.
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy wird importiert, um die Interaktion mit der Datenbank zu verwalten.


app = Flask(__name__) # wird als Instanz von Flask erstellt und konfiguriert
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medications.db' # Hier wird eine SQLite-Datenbank namens medications.db im aktuellen Verzeichnis verwendet
app.config['SECRET_KEY'] = 'your_secret_key' # geheime Zeichenfolge, die für CSRF-Schutz und andere Sicherheitsmechanismen in Flask verwendet wird
db = SQLAlchemy(app) # db wird als Instanz von SQLAlchemy erstellt und mit der Flask-Anwendung app verbunden