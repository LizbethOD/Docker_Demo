import web 

render_app = web.template.render("templates/")

class index():
    def GET(self):
        return render_app.index()