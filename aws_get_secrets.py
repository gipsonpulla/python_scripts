import boto3
import json

def get_secret():
    secret_name = "my-app/prod/database-credentials"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except Exception as e:
        # Handle exceptions like ResourceNotFoundException, DecryptionFailureException, etc.
        raise e
    else:
        # Depending on whether the secret is a string or JSON, retrieve accordingly
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        else:
            # For binary secrets, use base64 decoding
            # ...
            pass

# In your main application logic
try:
    db_secrets = get_secret()
    # Use the secrets for your database connection
    # db_username = db_secrets['username']
    # db_password = db_secrets['password']
    # ...
except Exception as e:
    print(f"Failed to retrieve secret: {e}")
