import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import boto3

s3 = boto3.client("s3",
                  region_name='us-east-2',
                  aws_access_key_id='AKIAZROUJCN5R7Q4423K',
                  aws_secret_access_key='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')


class DatetimeEncoder(json.JSONEncoder):
    try:
        def default(self, obj):
            try:
                return super().default(obj)
            except TypeError:
                return str(obj)
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


def list_all_objects():
    try:
        return s3.list_objects(Bucket='picusfurkan')
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


def send_JSON(body_dict):
    try:
        new_key = list(body_dict.keys())[0]
        s3.put_object(
            Body=json.dumps(body_dict.get(new_key)),
            Bucket='picusfurkan',
            Key=new_key

        )
        return new_key
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


def read_obj(key):
    try:
        obj = s3.get_object(
            Bucket='picusfurkan',
            Key=key
        )
        return obj['Body'].read().decode('utf-8')
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/picus/list'):
                output_dict = s3.list_objects(Bucket='picusfurkan')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(json.dumps(output_dict, cls=DatetimeEncoder).encode('utf-8'))
            elif self.path.count('/picus/list/'):
                key = self.path.split("/")[-1]
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(read_obj(key).encode('utf-8'))
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)

    def do_POST(self):
        try:
            if self.path.endswith('/picus/put'):
                content = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode("UTF-8"))
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(send_JSON(content).encode('utf-8'))
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)


def main():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    server.allow_reuse_address = True
    try:
        server.serve_forever()
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)


if __name__ == '__main__':
    main()
