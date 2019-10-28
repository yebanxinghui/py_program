#对http://www.something.com形式的URL进行分割

url=input('Please enter the URL: ')
domain=url[11:-4]

print("Domain name: " +domain)
