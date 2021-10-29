# Инкапсуляция.

# class VkAccountInWebSite:

#     def __init__(self, name, login_id, password):
#         self.__name = name
#         self.__login_id = login_id
#         self.__password = password

#     def publicLogin(self):
#         self.__loginVk()

#     def __loginVk(self):
#         if self.__login_id == 123 and self.__password == 456:
#             print("Привет " + self.__name)
#         return True


# vkakk = VkAccountInWebSite("Art", 123, 456)
# vkakk.publicLogin()

class New:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name



new_obj = New("Иван")
print(new_obj)

