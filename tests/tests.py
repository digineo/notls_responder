import sys
import unittest
import os
import subprocess
sys.path = sys.path+["../."]
from tls_responder import TLSresponder, AbortReply, DisallowedHeaderException, TestMailSender

class Test_tls_responder(unittest.TestCase):
    def setUp(self):
        # try:
        #     os.remove("./.tmp/tls_respons.eml")
        # except:
        pass
    #	self.respons = TLSresponder(incommingmail)
    def tearDown(self):
        # try:
        #     os.remove("./.tmp/tls_respons.eml")
        # except:
        pass
    

    #BlackBoxing
    def AbortReply(self, path):
        try:
            respons = TLSresponder(path, TestMailSender)
            re_val = respons.send_mail()
            return re_val
        except AbortReply, e:
            re_val = e.reason
            return re_val
        except DisallowedHeaderException, e:
            re_val = e.reason 
            return re_val


    def test_abbort_if_header_not(self):
        #respons = TLSresponder("")
        re_val = self.AbortReply("./drop/mailer_daemon.eml")
        assert("disallowed header" in re_val)

    def test_abbort_if_header(self):
        re_val = self.AbortReply("./drop/mailer_daemon.eml")
        assert("disallowed header" in re_val)

    def test_no_subject(self):
        re_val = self.AbortReply("./drop/no_subject.eml")
        assert(re_val == "dropped, subject missing")

    def test_disallowed_adress(self):
        re_val = self.AbortReply("./drop/mailer_daemon2.eml")
        assert(re_val == "dropped, disallowed address")

    def test_locally_send_output(self):
        re_val = self.AbortReply("./drop/locally_delivered.eml")
        assert(re_val == "dropped, locally delivered")
    

    def test_with_tls_output(self):
        re_val = self.AbortReply("./drop/with_tls.eml")
        
        assert(re_val == "dropped, is send with tls")
    


    def test_nothing_thrown(self):
        re_val = self.AbortReply("./reply/no_tls.eml")
        assert("Dave <dave@example.com>" in re_val)

if __name__ == '__main__':
    unittest.main()
    