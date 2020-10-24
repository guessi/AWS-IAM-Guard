# AWS IAM Guard
 
![https://img.shields.io/badge/Python-3.7%2b-blue](https://img.shields.io/badge/Python-3.7%2b-blue)
![https://img.shields.io/github/license/guessi/AWS-IAM-Guard](https://img.shields.io/github/license/guessi/AWS-IAM-Guard)

AWS IAM Guard with Slack integration support

# Description

With organization growth, more and more IAM user(s) created, security audit
becomes a must action, but it is hard to do security audit manually,
*AWS IAM Guard* is trying to solve this problem in programmatic way.

# Supported Audit Items

- IAM User with no MFA configured
- IAM User with no access history for N-day _(TODO)_
- IAM User's password age over N-day _(TODO)_
- IAM User's Access Key's age over N-day _(TODO)_
- IAM User's Access Key have no access history for N-day _(TODO)_
- IAM User with no access history for N-day _(TODO)_
- IAM User with no policy attached _(TODO)_
- IAM Group with no member _(TODO)_
- IAM Group with no policy attached _(TODO)_
- IAM Policy with no usage _(TODO)_

# Requirements

- Python 3.7+
- AWS profile(s) configured
- Slack webhook configured

# Usage

    $ pip3 install -r requirements.txt
    $ cp local_settings.py.example local_settings.py
    $ vim local_settings.py
    $ python3 ./aws-iam-guard.py

# FAQ

How do I configure a named AWS profile?

    https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

Where can I find my incoming webhook?

    https://<your-namespace>.slack.com/apps/manage/custom-integrations

# Reference

- [AWS IAM Best Practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Security Audit Guidelines](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)
- [Slack Webhook](https://api.slack.com/messaging/webhooks)

# License

[GPL-3.0 License](LICENSE)
