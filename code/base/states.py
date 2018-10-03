class BaseCommand(object):

    def __init__(self):
        pass

    def __call__(self, state):
        pass


class BaseState(object):

    def __init__(self, eventlog=None, user=None):
        self.eventlog = eventlog
        self.user = user
        self.state = self

    def init(self):
        pass

    def rebuild(self, version=None):
        self.init()
        for event in self.eventlog.objects.created_by(self.user).order_by('id'):
            self.state.handle(event)
        return self

    def set_state(self, state):
        self.state = state

    def nohandle(self, event):
        print("No handler for {} in state {}".format(event.event, self.state))
        return False

    def handle(self, event):
        method = getattr(self.state, event.event, self.nohandle)
        return method(event)

    def execute(self, command):
        event = command(self)
        if event:
            event = self.handle(event)
            event.save()
            return True

        return False
