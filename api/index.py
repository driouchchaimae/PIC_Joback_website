import json
from http.server import BaseHTTPRequestHandler
from ugropy import joback


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            name = str(payload.get("nom", "")).strip()

            if not name:
                raise ValueError("Veuillez saisir le nom d'une molécule.")

            molecule = joback.get_groups(name)
            temperature = molecule.normal_boiling_point

            result = {
                "success": True,
                "nom": name,
                "groupes": str(molecule.subgroups),
                "temperature": temperature,
            }
            self._send_json(200, result)

        except Exception as exc:
            self._send_json(400, {
                "success": False,
                "erreur": str(exc) or "Molécule non reconnue ou groupes indisponibles."
            })

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Allow", "POST, OPTIONS")
        self.end_headers()

    def _send_json(self, status, data):
        body = json.dumps(data, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
