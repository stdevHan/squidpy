from squidlog import squid, compareUser

squid('access.log.1', 'excludes', 'user')
compareUser('user', 's')
