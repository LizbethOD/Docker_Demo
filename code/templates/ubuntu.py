import web 

render_app = web.template.render("templates/")

class ubuntu():
    def GET(self):
        return render_app.ubuntu()