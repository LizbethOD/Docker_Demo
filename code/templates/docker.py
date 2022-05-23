import web 

render_app = web.template.render("templates/")

class docker():
    def GET(self):
        return render_app.docker()