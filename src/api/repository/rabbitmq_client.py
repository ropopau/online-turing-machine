import pika


class RabbitMQClient():
    def __init__(self, host="localhost"):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="turing_steps")

    def consume_steps(self, callback):
        self.channel.basic_consume(
            queue="turing_steps",
            on_message_callback=callback,
            auto_ack=True
        )
        self.channel.start_consuming()

    def close(self):
        self.connection.close()