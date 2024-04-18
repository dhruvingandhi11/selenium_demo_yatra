

class Utils():
    
    def assert_list_item_txt(self,list,value): 
        for stop in list:
            try:
                print(f"{stop.text= }")
                assert stop.text == value
                print("Assertion passed")
            except:
                print("Assertion failed")