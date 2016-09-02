# coding:utf-8
import tornado
import tornado.web
import tornado.template
from src import (config, routes)
import os
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options



def check_self():
    '''
    check_self config and dependent
    :return:
    '''
    pass


def info(str):
    '''
    :param str:
    :return:
    '''
    print str


def config_yaml():
    '''
    config the App value
    :return:
    '''
    import yaml

    yaml_config = yaml.load(open("./config.yaml"))
    for key in yaml_config.keys():
        # os.environ[key.upper()]=yaml_config[key]
        if not os.environ.has_key(key.upper()):
            os.environ[key.upper()] = str(yaml_config[key])
            if key == "project_dir":
                os.environ[key.upper()] = os.getcwd() + "/"
            if key == "storage_index_db":
                os.environ[key.upper()] = os.getcwd() + "/" + str(yaml_config[key])
            if key == "template":
                os.environ[key.upper()] = os.getcwd() + "/" + str(yaml_config[key])


config_yaml()

route = routes.getRoutes(config)


class Application(tornado.web.Application):
    def __init__(self):
        # urls settings
        # handlers = 
        ''' the setting '''
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "webapp/templates"),
            static_path=os.path.join(os.path.dirname(__file__), "webapp/static"),
            # 防跨站伪造请求
            xsrf_cookies=False,
            cookie_secret="test-2001",
            login_url="/login",
            debug=True,                  #调试模式
        )
        # 服务器初始化
        tornado.web.Application.__init__(self, handlers=route, **settings)
        
# start run
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(5555)
    tornado.ioloop.IOLoop.instance().start()

# main run
if __name__ == "__main__":
    main()
        
# application = tornado.web.Application(route)

# if __name__ == "__main__":
#     # settings = {'debug': True}
#     check_self()
#     info('config successful ... ')

#     application.listen(os.environ[config.PROJECT_PORT])
#     application.debug = True
#     # application.autoreload=False
#     info('Picture-Compare service runing ...')
#     tornado \
#         .ioloop \
#         .IOLoop \
#         .current() \
#         .start()
