import requests
import sys


class Webhook:

    def get_all_webhooks(self):
        """
        GETS A LIST OF ALL THE WEBHOOKS CURRENTLY CONNECTED TO YOUR BOT
        uses the https://api.ciscospark.com/v1/webhooks - GET request
        details on the list webhooks URL can be found in https://developer.webex.com/docs/api/v1/webhooks/list-webhooks
        """

        url_route = "webhooks"

        data = requests.get(self.URL + url_route, headers=self.headers)

        return data

    def create_webhook(self, name=None, target_url=None, resource=None, event=None):
        """
        Enables one to create a webhook that will be listening to events sent to the bot
        uses the https://api.ciscospark.com/v1/webhooks - POST request
        details on create webhooks URL can be found in https://developer.webex.com/docs/api/v1/webhooks/create-a-webhook
        """

        url_route = "webhooks"

        if name is None:
            sys.exit("'name' is a required field")

        elif target_url is None:
            sys.exit("'targetUrl' is a required field")

        elif resource is None:
            sys.exit("'resource' is a required field")

        elif event is None:
            sys.exit("'event' is a required field")

        # check for if a webhook with this URL already exists for this particular bot
        # cause apparently Cisco does not do that for us when creating webhooks. But tis all good :)
        existing_webhooks = self.get_all_webhooks().json()
        for webhook in existing_webhooks['items']:
            if webhook['targetUrl'] == target_url:
                return self.get_webhook_details(webhook_id=webhook['id'])

        json = {
            "name": name, "targetUrl": target_url, "resource": resource, "event": event
        }

        data = requests.post(self.URL + url_route, headers=self.headers, json=json)
        return data

    def delete_webhook(self, webhook_id=None):
        """
        Deletes a webhook that has ID webhookId
        uses the https://api.ciscospark.com/webhooks - DELETE request
        details on delete webhooks URL can be found in https://developer.webex.com/docs/api/v1/webhooks/delete-a-webhook 
        """

        url_route = "webhooks"

        if webhook_id is None:
            sys.exit("'webhookId' is a required field")

        data = requests.delete(self.URL + url_route + "/" + webhook_id, headers=self.headers)
        return data

    def update_webhook(self, webhook_id=None, name=None, target_url=None):
        """
        'name' is the updated name of the webhook
        'targetUrl' is the updated targetUrl of the webhook

        Edit a webhook with ID of webhookId
        uses the https://api.ciscospark.com/webhooks - PUT request
        details on edit webhook URL can be found in https://developer.webex.com/docs/api/v1/webhooks/update-a-webhook
        """

        url_route = "webhooks"

        if webhook_id is None:
            sys.exit("'webhookId' is a required field")

        elif name is None:
            sys.exit("'name' is a required field")

        elif target_url is None:
            sys.exit("'targetUrl' is a required field")

        json = {
            "name": name, "targetUrl": target_url
        }

        data = requests.put(self.URL + url_route + "/" + webhook_id, json=json, headers=self.headers)
        return data

    def get_webhook_details(self, webhook_id=None):
        """
        Get the details of a single webhook with id of webhookId
        uses https://api.ciscospark.com/webhooks/{roomId} - GET request
        details on get webhook details URL can be found in https://developer.webex.com/docs/api/v1/webhooks/get-webhook-details 
        """

        url_route = "webhooks"

        if webhook_id is None:
            sys.exit("'webhookId' is a required field")

        data = requests.get(self.URL + url_route, headers=self.headers)
        return data
