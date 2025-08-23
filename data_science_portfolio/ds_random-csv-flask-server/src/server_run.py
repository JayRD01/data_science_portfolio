from .singleton_contract import SingletonContract, SingletonInterface
from flask import Flask, send_from_directory

@SingletonContract
class ServerFlask(SingletonInterface):
    """
    Singleton class that launches a simple Flask server to serve a CSV file
    from a given folder.
    """
    def __init__(self, folder: str, file: str):
        self.folder: str = folder  # Directory where the file is stored
        self.file: str = file      # Filename to serve
        self.app: Flask = Flask(__name__)  # Flask app instance
        self.setup_routes()        # Auto-load routes on init

    def setup_routes(self) -> None:
        """
        Defines the available routes of the server.
        """
        @self.app.route("/csv")
        def csv_return():
            # Serves the file as a download (Content-Disposition: attachment)
            return send_from_directory(
                directory=self.folder,
                path=self.file,
                as_attachment=True
            )

    def run(self, host: str = "0.0.0.0", port: int = 8090) -> None:
        """
        Starts the Flask server and listens on the specified host and port.
        """
        print(f"✅ Server started at http://{host}:{port}/csv")
        self.app.run(host=host, port=port)
