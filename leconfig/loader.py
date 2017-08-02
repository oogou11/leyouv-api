import types
import logging

logger = logging.getLogger('leconfig')

def load_to_dict(d, text=None, filename=None,
                 s3_bucket=None, s3_key=None):
     if text:
         pass
     elif filename:
         text = open(filename).read()
     else:
         text = ''
     code_obj = compile(text, "<config string>", 'exec')
     exec(code_obj, d)
     for (k, v) in d.items():
         logger.info("%s = %s" % (k, repr(v)))