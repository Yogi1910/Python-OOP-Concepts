class EmailNotification:
    def send(self):
        return "Sending Email Notification..."


class SMSNotification:
    def send(self):
        return "Sending SMS Notification..."

def notify(service):
    return service.send()


if __name__ == "__main__":
    email = EmailNotification()


    print(notify(email))