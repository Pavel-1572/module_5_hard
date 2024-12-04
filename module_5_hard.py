import time


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname,hash(password)) == user.get_nickname_password():
                self.current_user = user
                return user

    def register(self, nickname, password, age,):
        user_new = User(nickname, password, age)
        if user_new not in self.users:
            self.users.append(user_new)
            self.current_user = user_new
        else:
            print(f'Пользователь {nickname} уже существует')


    def log_out(self):
        self.current_user = None

    def add(self, *other):
        for video in other:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        word_list = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                word_list.append(video.title)
        return word_list

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=" ")
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname
    def __eq__(self, other):
        return other.nickname == self.nickname
    def get_nickname_password(self):
        return self.nickname, self.password


class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

