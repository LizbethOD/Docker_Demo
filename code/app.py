import web

urls = ( 
    "/index", "templates.index.index",
    "/docker", "templates.docker.docker",
    "/ubuntu", "templates.ubuntu.ubuntu",

)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()