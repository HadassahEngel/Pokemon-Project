from configure import port_number
from server import app

if __name__ == '__main__':
    app.run(port=port_number)