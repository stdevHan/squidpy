class user():
    user = ''
    ips = []
    size = 0

    def __init__(self):
        self.user = ''
        self.ips = []
        self.size = 0

    def setuser(self, puser):
        self.user = puser

    def addips(self, ip):
        for p in self.ips:
            if p == ip:
                return
        self.ips.append(ip)

    def setips(self, ips):
        self.ips = ips

    def addsize(self, size):
        self.size = self.size + size

    def setsize(self, size):
        self.size = size


class userlist():
    users = []

    def __init__(self):
        self.users = []

    def setuserfull(self, puser):
        for i in range(len(self.users)):
            if self.users[i].user == puser.user:
                self.users[i].setsize(puser.size)
                self.users[i].setips(puser.ips)
                return
        self.users.append(puser)

    def setuser(self, puser):
        flag = False
        tmpuser = user()
        tmpuser.user = puser
        for p in self.users:
            if p.user == tmpuser.user:
                flag = True
        if not flag:
            self.users.append(tmpuser)

    def getUser(self, users):
        for p in self.users:
            if p.user == users:
                return p
        return 1


def compareUser(pathuser, users):
    user = open(str(pathuser))
    for a in user:
        print a


def squid(pathlog, pathexclude, pathuser):
    users = userlist()
    f = open(str(pathlog))
    # excludes = open(str(pathexclude)) by not used for now
    for a in f:
        text = a.split(' ')
        if len(text) == 11 and (text[4] == 'TCP_TUNNEL/200' or text[4] == 'TCP_MISS/200'):
            users.setuser(text[8])
            puser = users.getUser(text[8])
            if puser != 1:
                puser.addips(text[3])
                puser.addsize(int(text[2]) + int(text[5]))
                users.setuserfull(puser)

    for p in users.users:
        print p.user + ' ' + str(p.size / 1024 / 1024) + 'MB'
        print p.ips
