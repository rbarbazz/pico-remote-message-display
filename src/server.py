from phew import server, access_point, logging
from phew.server import serve_file


@server.route("/", methods=["GET", "POST"])
def index(request):
    if request.method == "GET":
        return serve_file("templates/index.html")
    if request.method == "POST":
        message = request.form.get("message")
        logging.debug(f"posted message: {message}")

        return serve_file("templates/posted.html")


@server.route("/global.css", methods=["GET"])
def styles(_):
    return serve_file("styles/global.css")


@server.catchall()
def catchall():
    return "Not found", 404


ap = access_point("Monkey123")

# TODO: print on display
print(ap.ifconfig()[0])

server.run()
