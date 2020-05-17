from app import app,db
from app.models import User, UsbMemory, Rireki

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UsbMemory': UsbMemory, 'Rireki': Rireki}

