from http import cookiejar

import mechanize


def login():
    br = mechanize.Browser()
    cj = cookiejar.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize.HTTPRefreshProcessor, max_time=1)
    br.set_debug_http(False)
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/71.0.3578.98 Safari/537.36')]
    br.open('https://accounts.douban.com/login')
    br.select_form(name='lzform')
    br.form['form_email'] = '2471788627@qq.com'
    br.form['form_password'] = 'zengjianrong55'
    response = br.submit()
    return response


response = login()
print(response.body)

