import time

from django.db.models.signals import post_save,pre_save

from django.core.signals import request_finished

from django.dispatch import receiver

from test_server.libs.apns import APNs, Frame, Payload
from django.conf import settings

from test_server.apps.message.models import Message
from test_server.apps.client.models import ClientToken
from test_server.settings.dev import CERT_PEM, KEY_PEM


@receiver(post_save, sender=Message,dispatch_uid="post_save")
def msg_send(sender, **kwargs):
    devices = ClientToken.objects.all()
    if devices is not None:
        apns = APNs(
            use_sandbox=True,
            cert_file=CERT_PEM,
            key_file=KEY_PEM)

        message = kwargs['instance']
        content = message.content

        frame = Frame()
        identifier = 1
        expiry = int(time.time() + 3600)
        priority = 10
        payload = Payload(
            alert=content,
            sound="default",
            badge=1,
            mutable_content=True)

        for device in devices:
            frame.add_item(
                device.msg_token,
                payload,
                identifier,
                expiry,
                priority)
        apns.gateway_server.send_notification_multiple(frame)

