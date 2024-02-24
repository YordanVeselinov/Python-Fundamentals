class Email:
    def __init__(self,sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
name = input()
while name != "Stop":
    sender, receiver, content = name.split()
    email = Email(sender,receiver,content)
    emails.append(email)
    name = input()


index = [int(x) for x in input().split(", ")]

for current_index in index:
    emails[current_index].send()
for current in emails:
    print(current.get_info())