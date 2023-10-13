import asyncio

from phew import server, access_point, logging, dns
from phew.server import serve_file
from phew.template import render_template

from tasks import process_message

AP_DOMAIN = "pico.local"


def redirect_to_ap_domain_decorator(fn):
    def redirect_to_ap_domain(request):
        if request.method == "GET" and request.headers.get("host") != AP_DOMAIN:
            return render_template("templates/redirect.html", domain=AP_DOMAIN)

        return fn(request)

    return redirect_to_ap_domain


@server.route("/", methods=["GET", "POST"])
@redirect_to_ap_domain_decorator
def index(request):
    if request.method == "GET":
        return serve_file("templates/index.html")
    if request.method == "POST":
        message = request.form.get("message")
        logging.debug(f"Posted message: {message}")
        asyncio.create_task(process_message(message))

        return serve_file("templates/posted.html")


@server.route("/global.css", methods=["GET"])
def styles(_):
    return serve_file("styles/global.css")


@server.catchall()
@redirect_to_ap_domain_decorator
def catchall(_):
    return "Not found.", 404


ap = access_point("White Rabbit")
ip = ap.ifconfig()[0]
dns.run_catchall(ip)

server.run()
