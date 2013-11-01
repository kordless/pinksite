import os, logging

# configuration for pinkpanter sample site

# application
app_name = "Pink Site"
app_admin_name = "Kord Campbell"
app_admin_email = "kordless@stackgeek.com"

# application contact form
app_contact_sender = "kordless@stackgeek.com"
app_contact_recepient = "kordless@stackgeek.com"

# Password AES Encryption Parameters
aes_key = "12_24_32_BYTES_KEY_FOR_PASSWORDS"
salt = "_PUT_SALT_HERE_TO_SHA512_PASSWORDS_"

# twitter credentials
twitter_consumer_key : 'PUT_YOUR_TWITTER_CONSUMER_KEY_HERE'
twitter_consumer_secret : 'PUT_YOUR_TWITTER_CONSUMER_SECRET_HERE'

# github credentials
github_server = 'github.com'
github_redirect_uri = 'http://www.example.com/social_login/github/complete'
github_client_id = 'PUT_YOUR_GITHUB_CLIENT_ID_HERE'
github_client_secret = 'PUT_YOUR_GITHUB_CLIENT_SECRET_HERE'

# google recaptcha
captcha_public_key = "PUT_YOUR_RECAPCHA_PUBLIC_KEY_HERE"
captcha_private_key = "PUT_YOUR_RECAPCHA_PRIVATE_KEY_HERE"

# google analytics
google_analytics_domain = "YOUR_PRIMARY_DOMAIN (e.g. google.com)"
google_analytics_code = "UA-XXXXX-X"
