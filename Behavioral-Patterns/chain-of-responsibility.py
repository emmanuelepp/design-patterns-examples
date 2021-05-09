# Chain of responsibility
# Lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.
class Handler:  # Abstract
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)  # Stop here

        if not handled:  # keep going
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Provide implementation in subclass')


class ConcreteHandlerOne(Handler):

    def _handle(self, request):

        if 0 < request <= 10:
            print('Request {} handled in handler one '.format(request))
            return True


class DefaultHandler(Handler):

    def _handle(self, request):
        print('End of chain, no handle for {} '.format(request))
        return True


class Client:
    def __init__(self):
        self.handler = ConcreteHandlerOne(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(requests)


# Create client
client = Client()

# Create request
requests = [1, 2, 3]

# Send request
client.delegate(requests)
