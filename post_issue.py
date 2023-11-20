from google.cloud import pubsub_v1

topic_name = "projects/mplus-video-conference-dev/topics/log_acquire"

publisher = pubsub_v1.PublisherClient()

message_data = "Request for Google Admin login logs."

future = publisher.publish(topic_name, data=message_data.encode("utf-8"))

future.result()

subscriber = pubsub_v1.SubscriberClient()

subscription_name = "projects/mplus-video-conference-dev/subscriptions/logs"

response = subscriber.pull(
    request={"subscription": subscription_name, "max_messages": 10}
)

for received_message in response.received_messages:
    message = received_message.message
    message_data = message.data
    print(f"Received message: {message_data.decode('utf-8')}")

    subscriber.acknowledge(
        request={"subscription": subscription_name, "ack_ids": [received_message.ack_id]}
    )

