class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content, time):
        self.posts.append(content)
        self.posts.append(time)
        print(f"{self.username} added a new post: {content} (time: {time})")

post1 = SocialMediaProfile('Jake')
post1.add_post('Hello, world!', "12:34")
post2 = SocialMediaProfile("Finn")
post2.add_post('Had a great day at the park!', "13:16")
post3 = SocialMediaProfile("Marcel")
post3.add_post("What's up, Natalie? How are you?", "17:52")
