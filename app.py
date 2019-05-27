import os
import app
import json

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name

def main():
    try:
        config = json.loads(open(real_path('/config/config.json')).read())
        inject_host = config['inject_host']
        inject_port = config['inject_port']
        app.inject(str(inject_host), int(inject_port)).start()
    except KeyboardInterrupt:
        pass
    except Exception as exception:
        app.log('Exception: {}'.format(exception), color='[R1]')
    finally: exit()

if __name__ == '__main__':
    main()
