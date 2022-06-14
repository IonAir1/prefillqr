import config

def generate_prefill(name, email):
    print(config.forms_link)
    url = config.forms_link.replace('=name', '=' + name)
    url = url.replace('=email', '=' + email)
    return(url)