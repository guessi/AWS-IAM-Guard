#!/usr/bin/env python3

import boto3
import local_settings as config

from datetime import datetime
from slack import WebhookClient
from slack.web.classes.attachments import Attachment, AttachmentField


def slackSend(fields: list) -> None:
    client = WebhookClient(url=config.webhook_url)
    client.send(
        attachments=[
            Attachment(
                author_name=config.author_name,
                thumb_url=config.thumb_url,
                footer=config.footer,
                footer_icon=config.footer_icon,
                text=config.text,
                ts=datetime.timestamp(datetime.now()),
                fields=fields,
            )
        ]
    )


def iamScan(profile: str) -> list:
    boto3.setup_default_session(profile_name=profile)
    iam = boto3.client('iam')

    users_raw = iam.list_users()['Users']
    mfa_devices = iam.list_virtual_mfa_devices()['VirtualMFADevices']

    users = [user['UserName'] for user in users_raw]
    with_mfa = [
        mfa['User']['UserName']
        for mfa in mfa_devices if mfa.get('User') is not None
    ]

    return [user for user in users if user not in with_mfa + config.excludes]


def getFields(profiles: list) -> list:
    fields = []

    for profile in profiles:
        users = iamScan(profile)
        msg = ""
        for user in users:
            msg += "- `{}`\n".format(user)

        fields.append(AttachmentField(title=profile.title(), value=msg))

    return fields


def main() -> None:
    fields = getFields(config.aws_profiles)
    slackSend(fields) if len(fields) > 0 else True


if __name__ == "__main__":
    main()
