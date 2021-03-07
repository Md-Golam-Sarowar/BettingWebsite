import random
import string
from BettingApp.models import Credential


def addCredentials(totalCredentials):

    Credential.objects.all().delete()
    credentials = []

    for i in range(0, totalCredentials):
        usernameRandom = "".join(random.choice(string.ascii_letters) for i in range(10))
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(password_characters) for i in range(8))
        role = "user"
        credentialObject = Credential(
            username=usernameRandom, password=password, role=role
        )
        credentialObject.save()
        credentials.append(usernameRandom)
        credentials.append(password)
        credentials.append(role)

    return credentials


def updateCredential(updatecredential, id):
    credential = Credential.objects.get(pk=id)
    credential.username = updatecredential[0]
    credential.password = updatecredential[1]
    credential.role = updatecredential[2]
    credential.save()
