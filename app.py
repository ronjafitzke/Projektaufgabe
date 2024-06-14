from shared import app
import medicationRoutes
import medicationRepository

if __name__ == "__main__":
    app.run(port=8000, debug=True)