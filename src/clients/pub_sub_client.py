from google.cloud import pubsub_v1


def publish_message(data):
    publisher = pubsub_v1.PublisherClient()
    topic_name = "projects/{project_id}/topics/{topic}".format(
        project_id="test-project", topic="test-topic"
    )
    future = publisher.publish(topic_name, data=data)
    future.result()
