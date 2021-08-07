from tests.test_app import TestrequestHandler

if (TestrequestHandler.do_GET("../picus/list"))=="202":
    print("fine")