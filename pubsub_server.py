import rpyc
from rpyc.utils.server import ThreadedServer


class PubSubService(rpyc.Service):

    def __init__(self):
        self.subscriptions = {}
    def exposed_subscribe(self, topic, callback):
        if topic not in self.subscriptions:
            self.subscriptions[topic] = []
        self.subscriptions[topic].append(callback)
        print(self.subscriptions[topic])
        print(f"Subscribed to topic '{topic}'")

    def exposed_publish(self, topic, message):
        print(self.subscriptions)
        if topic in self.subscriptions:
            for callback in self.subscriptions[topic]:
                callback(message)
            print(f"Published '{message}' to topic '{topic}'")
        else:
            print(f"No subscribers for topic '{topic}'")

if __name__ == "__main__":
    server = ThreadedServer(PubSubService, port=18861, protocol_config={"allow_public_attrs" : True})
    server.start()
