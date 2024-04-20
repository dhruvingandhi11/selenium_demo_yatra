import softest

class Utils(softest.TestCase):
    
    def assert_list_item_txt(self,list,value): 
        for stop in list:
            # try:
            print(f"{stop.text= }")
            # assert stop.text == value
            self.soft_assert(self.assertEqual, stop.text, value)
            print("Assertion passed")
            if stop.text == value:
                print("Assertion passed")
            else:
                print("Assertion failed")
        self.assert_all()
            # except:
            #     print("Assertion failed")