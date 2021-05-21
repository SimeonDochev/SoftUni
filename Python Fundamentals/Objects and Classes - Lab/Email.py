class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []
email_data = input()

while not email_data == "Stop":
    s, r, c = email_data.split()
    current_email = Email(s, r, c)
    emails_list.append(current_email)
    email_data = input()

indexes_of_sent_emails = [int(el) for el in input().split(", ")]

for i in indexes_of_sent_emails:
    Email.send(emails_list[i])

for email in emails_list:
    print(Email.get_info(email))
