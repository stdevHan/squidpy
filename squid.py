from squidlog import squid, compareUser

squid('access.log.1', 'exclude', 'user')
compareUser('user', 's')
