import http .server
import socketserver
from http import HTTPStatus
import io
import traceback
from contextlib import redirect_stdout
import time
class PrintServer (http .server .SimpleHTTPRequestHandler ):
    def do_GET (self ):
        self .send_response (HTTPStatus .OK )
        self .content_type ='текст/html; кодировка = utf-8'
        with io .StringIO ()as buf ,redirect_stdout (buf ):
            returnedbuf =None
            try :
                result =self .work ()
                if result is not None :
                    (returnedbuf ,content_type )=result
                    if content_type is not None :
                        self .content_type =content_type
            except Exception as e :
                print ("<предварительно>")
                print (traceback .format_exc ())
                print ("</pre>")
            resultbuf =None
            if returnedbuf is not None :
                resultbuf =returnedbuf
            else :
                resultbuf =buf .getvalue ().encode ('utf-8')
            self .send_header ('content-type',self .content_type )
            self .send_header ('content-length','{}'.format (len (resultbuf )))
            self .end_headers ()
            self .wfile .write (resultbuf )
    def work (self ):
        print ("Не реализован метод «работа»")
def start_server (worker_type ,port =81 ):
    for i in range (100 ):
        try :
            httpd =socketserver .TCPServer (('',port ),worker_type )
            httpd .serve_forever ()
        except OSError as e :
            if e .errno !=98 :
                break
            print ("Ожидание порта {} секунды.".format (i ,port ))
            time .sleep (1 )
        except KeyboardInterrupt :
            httpd .shutdown ()
            print ("\nСервер успешно завершен")
            break