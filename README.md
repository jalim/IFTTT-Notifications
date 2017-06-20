# IFTTT-Notifications
IFTTT Push Notifications for Craftbeerpi

This allows you to send any messages that appear in Craftbeerpi to IFTTT through their maker service.  You can then do whatever you like within IFTTT to this.

Setup:

1. Install this plugin within CBPI
2. Go to https://ifttt.com/maker_webhooks to connect the maker service
3. Create an IFTTT Applet that listens for a Webhook then outputs value1 (the title of the message) and value2 (the body of the message) to the service of your choice.  I use the Notifications service which sends an instant notification to my iphone with IFTTT installed.  You could also choose to send emails, have it posted on twitter or make your light globes flash.  The possibilities are endless.
4. Input your chosen Event Name and your Maker Webhook Key into the Craftbeerpi parameters page.
5. Reboot your system.
6. Everything should now be pushed to your chosen service.
