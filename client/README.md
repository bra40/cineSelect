# Run Flask
cd flask && export FLASK_APP=server.py && flask run

cd flask
export FLASK_APP=server.py
flask run

export FLASK_APP=server.py && flask run

---
if [ "$(pwd)" != "/Users/brunoarnabar/Documents/Websites/CineSelect/flask" ]; then
  cd flask && export FLASK_APP=server.py && flask run
else
  export FLASK_APP=server.py && flask run
fi

# Run Client
cd client && npm start

cd client
npm start

# Run Python
cd flask && source venv/bin/activate

cd flask
source venv/bin/activate

# Exit Python
Ctrl+d
deactivate