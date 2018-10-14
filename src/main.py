import falcon


class Pollos(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "What is that?\n"


app = falcon.API()

pollos_resource = Pollos()

app.add_route("/", pollos_resource)
