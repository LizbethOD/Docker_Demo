import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'Liz'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()