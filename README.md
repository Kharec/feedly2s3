## What

Do you know [Feedly](https://feedly.com) ? Good. And do you use it ? Better.

`feedly2s3` uses the Feedly's API to export an OPML file which contains the lists of your Feedly's subscriptions, and uploads it to the S3 bucket of your choice. 

## Installation

It needs mainly `boto3` and `requests` python modules, which you can both install with:

~~~bash
$ pip install -r requirements.txt
~~~

You're also gonna need :
* a IAM user which has `AmazonS3FullAccess` right
* your AWS credentials up to date in `~/.aws/credentials`
* a feedly developer token, which you can get [here](https://feedly.com/v3/auth/dev)

You can create those two from [the AWS management console](https://console.aws.amazon.com).

For the IAM role, go to [IAM](https://console.aws.amazon.com/iam/) > Roles > Create role > choose Transfer > Give AmazonS3FullAccess right > No tag > Give it a name > Create a role.

You can do the whole "install" thing by `./install.sh` : it'll ask you for your Feedly's credentials and your S3 bucket name, and put the script in `/opt/bin` without the `.py` extension.

## How it works

In fact, `feedly2s3` uses the `requests` python module to call the Feedly's API with your token, more specificaly the `/v3/opml` route, and saves the content in a temporary file. Then, it uses `boto3` to upload it to your s3 bucket.

Once it's installed, it runs with no arguments. You can call it like me, in a cron every 2 days:

~~~cron
0 6 * * 0,2,4,6 /opt/bin/feedly2s3
~~~

Or you can just call it from time to time, as you wish.

## Licence & Copyright
This software is copyright (c) 2020 by Sandro CAZZANIGA.

This is free software, you can use/redistribute it and/or modify it under the GNU GPLv3 terms.
