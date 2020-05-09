from fbs_runtime.application_context.PyQt5 import ApplicationContext


class AppContext(ApplicationContext):
    def run(self):
        return self.app.exec_()

    def icon(self):
        return self.get_resource("images/icon.png")
