import json

IP_LIST_FILE = "list.json"

class SecuritySystem :
    # kara listeye ekleme metodu
    def add_to_blacklist(self,ip) :
        try :
            with open(IP_LIST_FILE,"r") as f :
                ip_list =  json.load(f)
                black_list = ip_list["blacklist"]

           
            if ip in black_list:
               print("-" * 30)            
               print("⚠️  This IP is already on the blacklist.")
               print("-" * 30)   
               return

            black_list.append(ip)
            print(black_list)
            
        # json dosyası yoksa  kendimiz oluşturuyoruz
        except FileNotFoundError :

            ip_list = {"blacklist": [], "whitelist": []}
            with open(IP_LIST_FILE, "w") as f:
                json.dump(ip_list, f, indent=4)
            print("⚠️ list.json not found. A new file has been created.")
            black_list = ip_list["blacklist"]  

        except json.JSONDecodeError as e :
            print(e)    


        with open(IP_LIST_FILE,"w") as f :
            json.dump(ip_list,f,indent=4)     
        

        print(f"✅ {ip} ıp address successfully added black list.")
        print("-" * 30)




    # beyaz listeye ekleme metodu
    def add_to_whitelist(self,ip) :

        try :
            with open(IP_LIST_FILE,"r") as f :
                ip_list =  json.load(f)
                white_list = ip_list["whitelist"]

            if ip in white_list:
                print("-" * 30)   
                print("⚠️  This IP is already on the whitelist")
                print("-" * 30)   
                return   
 
            white_list.append(ip)
            print(white_list)
            
        # json dosyası yoksa  kendimiz oluşturuyoruz
        except FileNotFoundError  :
            ip_list = {"blacklist": [], "whitelist": []}

            with open(IP_LIST_FILE, "w") as f:
                json.dump(ip_list, f, indent=4)

            print("⚠️ list.json not found. A new file has been created.")
            
            white_list = ip_list["whitelist"]  

        except json.JSONDecodeError as e :
            print(e)    


        with open(IP_LIST_FILE,"w") as f :
            json.dump(ip_list,f,indent=4)     
        
        print(f"✅ {ip} ıp address successfully added white list.")




    # erişim kontroş metodu
    def check_access(self,ip) :
        try :
            with open(IP_LIST_FILE,"r") as f :
                ip_list =  json.load(f)
                black_list = ip_list["blacklist"]
                white_list = ip_list["whitelist"]

            if ip in black_list :
                print(f"❌ Blocked.Because the ip address ({ip}) is blacklisted")
            elif ip in white_list :
                print("✅ Authorised")
            else :
                print("🤔 Unknown ip.Ip is not on any list")    
           
            
        # json dosyası yoksa  kendimiz oluşturuyoruz
        except FileNotFoundError  :
            ip_list = {"blacklist": [], "whitelist": []}

            with open(IP_LIST_FILE, "w") as f:
                json.dump(ip_list, f, indent=4)

            print("⚠️ list.json not found. A new file has been created.")

            black_list = ip_list["blacklist"] 
            white_list = ip_list["whitelist"]

        except json.JSONDecodeError as e :
            print(e)    




    # ip listesini listeleme metodu
    def show_lists(self) :
        # Listeleniyor
        try :
            with open(IP_LIST_FILE,"r") as f :
                ip_list =  json.load(f)
                black_list = ip_list["blacklist"]
                white_list = ip_list["whitelist"]


            print("-" * 70)   
            
            print(f"black list => {black_list}")

            print("-" * 70)   

            print(f"white list => {white_list}")

            print("-" * 70)   

        # json dosyası yoksa  kendimiz oluşturuyoruz
        except FileNotFoundError :
            ip_list = {"blacklist": [], "whitelist": []}

            with open(IP_LIST_FILE, "w") as f:
                json.dump(ip_list, f, indent=4)

            print("⚠️ list.json not found. A new file has been created.")

            black_list = ip_list["blacklist"] 
            white_list = ip_list["whitelist"]
        except json.JSONDecodeError as e :
            print(e)    




    # ip silme metodu
    def delete_ip(self,ip) :
        # ip silme kısmı
         try :
            with open(IP_LIST_FILE,"r") as f :
                ip_list =  json.load(f)
                black_list = ip_list["blacklist"]
                white_list = ip_list["whitelist"]

            if ip in black_list :
                print("-" * 60)   

                black_list.remove(ip)
                print("Successfully deleted blacklisted ip address.")
                print(black_list)

                print("-" * 60)   


            elif ip in white_list :
                print("-" * 60)   
                 
                white_list.remove(ip)
                print("Successfully deleted whitelisted ip address")
                print(white_list)

                print("-" * 60)   


            else :
                print("-" * 60)   
                print("Unknown ip.Ip is not on any list.")
                print("-" * 60)   
        # ip silme kısmı

        # json dosyası yoksa  kendimiz oluşturuyoruz
         except FileNotFoundError :
            ip_list = {"blacklist": [], "whitelist": []}

            with open(IP_LIST_FILE, "w") as f:
                json.dump(ip_list, f, indent=4)
                
            print("⚠️ list.json not found. A new file has been created.")

            black_list = ip_list["blacklist"] 
            white_list = ip_list["whitelist"]
        
         
         except json.JSONDecodeError as e :
            print(e)    


         with open(IP_LIST_FILE,"w") as f :
             json.dump(ip_list,f,indent=4)    


# ip kontrol metodu.Geçerli oktet olup olmadığı,oktet aralığı.
def ip_control() :
    while True :
        ip_address = input("Please enter a valid IP address : ").strip("")

        octets = ip_address.split(".")

        if len(octets) != 4:
            print("IP address length is invalid! Must consist of at least 4 octets.")
            continue

        is_valid = True
        for octet in octets :
            if not octet.isdigit() :
                print("The IP address is not a number! Please enter it again.")   
                is_valid = False
                break 
            

            if not (0 <= int(octet) <=255) :
                print("Invalid IP range!Valid range 0-255.")  
                is_valid = False
                break

        if is_valid : 
            break

    return ip_address         


          







def main_menu() :
 while True :
    print("1-Add to black list")
    print("2-Add to white list")
    print("3-Check")
    print("4-Show list")
    print("5-Delete ip")
    print("6-Exit")


    selection = input("Select  : ").strip()

    security = SecuritySystem()

    if selection == "1" :  
         valid_ip = ip_control()
         security.add_to_blacklist(valid_ip)
    
    elif selection == "2" :
         valid_ip = ip_control()
         security.add_to_whitelist(valid_ip)
  
    elif selection == "3" :
         valid_ip = ip_control()
         security.check_access(valid_ip)
  
    elif selection == "4" :    
         security.show_lists()
         
    elif selection == "5" :
         valid_ip = ip_control()
         security.delete_ip(valid_ip)  

    elif selection == "6" :
         print("successfully exited")   
         break

    else :
        print("-" * 30)   
        print("invalid selection. Try again.")
        print("-" * 30)   
      



if __name__ == "__main__" :
  main_menu()
