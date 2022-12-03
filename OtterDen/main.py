#Copyright ByteOtter (c) 2021-2022

from otter_den import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
