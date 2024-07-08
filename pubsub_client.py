import rpyc

class SubscriberClient(rpyc.Service):
    def __init__(self):
        super().__init__()

    def on_connect(self, conn):
        self.conn = conn

    def exposed_handle_message(self, message):
        print(f"Received message: {message}")

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 18861)
    service = conn.root
    subscriber = SubscriberClient()

    # Example: Subscribe to a topic
    service.subscribe("example_topic", subscriber.exposed_handle_message)

    # Now this subscriber is subscribed to receive messages for "example_topic"

    service.publish("example_topic", "Hello World!")

    conn.close()
