from urlparse import urlparse


# GET SUBDOMAIN NAME (name.example.com)

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# GET DOMAIN NAME (example.com)

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


print get_domain_name('https://www.hackerearth.com/sprints/ibmkone-hack/dashboard/AlphaQ/idea/')
