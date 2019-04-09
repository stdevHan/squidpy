import re
import urllib2

# regex for extracting header from either start of line or "- " up to a colon
header_re = re.compile('(?:^|(?:- ))([^\s\.:]+):')


def parseLogLine(t):
    "Take a squid log line and return a dictionary of header:value"
    parse_dict = {}
    # unquote %0A etc to get normal lines chars and split
    encoded_lines = urllib2.unquote(t).split('\r\n')

    for l in encoded_lines:
        # regex match for header
        m = header_re.search(l)

        # check we find a match extract the header string
        # and value string

        if m is not None:
            header_key = m.group(1)
            value = l[m.end():]
            parse_dict[header_key] = value

    return parse_dict
