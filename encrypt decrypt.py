import caesarcipher,time
from caesarcipher import CaesarCipher
class Securing_Caesar_Cipher:
    def __init__(self):
        self.banner='''

           __      ____             ___    _____     __           ___         ___                  ___               
         (        (    )   \  /    |   )     |     (    )       (            |   )       /\       |   )    |   |     \   /
        (         (__ /     \/     |__ )     |    (      )     (  ____       |__ )      /  \      |__ )    |___|      \ /
        (         | \        |     |         |    (      )      (     |      |\        / __ \     |        |   |       / 
         ( __     |  \       !     |         |     ( __ )        (_   |      |  \     /      \    |        |   |      /


'''
        self.banner2='''
                     __                                           __
                    |     Parameters        Use                     |
                    |                                               |
                    |           e=         Encode the message       |         
                    |                                               |
                    |         d =        decode the Message         |            
                    |                                               |
                    |         exit =     Quit the Program           |             
                    |                                               |
                    |                                               |
                    |                                               |
                    |__                                           __|
        '''
        self.encoding='''
    
                 ######       #      #            ######               % % % %            # # # # #           ######## 
                 #            # #    #           %                   %         %        #   #       #         #
                 #            #  #   #          %                   %           %           #        #        #
                 ######       #   #  #          %                   %           %           #         #       ######
                 #            #    # #          %                    %         %            #         #       #
                 #            #     ##           %                    %       %         #   #       #         #
                 ######       #      #            %%%%%%%              % % % %            # # # # #           ########



   '''
        self.decode='''
                 
                 
                 
                 
                 

            # # # #            ########              % % % %              %  %  %              # # # #           ####### 
         #  #       #          #                   %                    %         %       #    #       #         #
            #        #         #                  %                    %           %           #        #        #
            #         #        ########           %                    %           %           #         #       ######
            #         #        #                   %                    %         %            #         #       #
         #  #        #         #                    %                    %       %         #   #       #         #
            #  # # #           #########             % % % %              % % % %            # # # # #           ########

												   
                  




'''
        print(self.banner)
        self.list=[]  
        self.list2=[]
        
        condition=True
        while condition == True:
            decion = input("\nDo yo want to encode or decode (e/d):")
            if decion == "e":
                print(self.encoding)
                encode = input("\nEnter the text to encode:")
                if encode == "":
                    print("Plain Text EXpect ! Invalied")
                
                key1 =  input("\nEnter the key value:")
                if  key1 == "" :
                    print("No input")
                    exit(0)
                if isinstance(key1, str) or isinstance(key1, float) or isinstance(key1, bin) or isinstance(key1,hash) or isinstance(key1,bytes):
                    print("Invalid Input")

                off1 = int(key1)
                c1 = CaesarCipher(str(encode), offset=off1)
                c2=c1.encoded
                print("\n")
                print("Cipher Text:""\t",c2)
                print("\n")
                print("CHAR  ", "   HEXA  ", "  BINARY",       "        Key  " ,"\t","Logic-Gate","\t","Result","\t","New-Cipher")

                for letter in c2:
                    self.a1=bin(int(ord(letter)))
                    self.a2=self.a1
                    self.a3 = self.a2[2:]
                    self.a4 = str(self.a3)
                    self.a5 = self.a4.rjust(8, "0")


                    self.a6=off1
                    self.a7=bin(int(self.a6))
                    self.a8=str(self.a7[2:])
                    self.a9=self.a8.rjust(8,'0')
              
                #Conversion of keys and bin to int form for bit opearation support
                    self.a10=int(self.a5,2)
                    self.a11=int(self.a9,2)
                    self.a12=self.a10^self.a11
                    self.a13=bin(int(self.a12))   # hwwsl   opptk
                    self.a14=self.a13[2:]
                    self.a15=str(self.a14)

                    self.a16=self.a15.rjust(8,'0')
                    self.a17=int(self.a16,2)
                    self.a18=chr(self.a17)
                    self.a19=self.list.append(str(self.a18))
                    print(letter, "\t ", ord(letter), "\t ", self.a5,"\t",self.a9,"\t","XOR","\t""\t",self.a16,"\t",self.a18 )
                    self.a20=''.join(self.list)
                    self.show=''.join(self.list)
                print("\n")
                print(" New Secured Caesar  Cipher Text:",self.show )

            if decion == "d":
                print(self.decode)
                decode=input("Enter the cipher text to decode:")

                if decode == "":
                    print("Plain Text EXpect ! Invalid")

                keyo=input("Enter the key of the Cipher:")

                if  keyo == "" :
                    print("No key input")
                    exit(0)
                key=int(keyo)
                print("CHAR  ", "   HEXA  ", "  BINARY", "\t", "key", "\t", "\t", "Logic-Gate", "\t", "Result", "\t", "Caesar-Cipher")

                for cipher in decode:
                    self.a21=bin(int(ord(cipher)))
                    self.a22=str(self.a21)
                    self.a23=self.a21[2:]
                    self.a24=int(ord(cipher))
                    self.a25=str(self.a23).rjust(8,"0")
                #key to bin
                    self.a26=bin(key)
                    self.a27=self.a26[2:]
                    self.a28=str(self.a27).rjust(8,"0")
                    
                # binary to int and key to int

                    self.a29=int(self.a28,2)            # key to int
                    self.a30=int(self.a25,2)            # bin to int of caesar text
                    self.a31=self.a29 ^self.a30


                    self.a32=bin(self.a31)
                    self.a33=self.a32[2:]
                    self.a34=str(self.a33)
                    self.a35=self.a34.rjust(8,"0") # bin result

                    self.a36=int(self.a35,2)
                    self.a37=chr(int(self.a36))


                #hex to bin
                    self.hex_to_bin=bin(ord(cipher))
                    self.bin_to_8bit=str(self.hex_to_bin[2:])
                    self.bin_to_8bit2=self.bin_to_8bit.rjust(8,"0")
                    self.append_to_list1=self.list2.append(chr(self.a31))
                    self.join_cipher=''.join(self.list2)

                    self.crack_caesar=CaesarCipher(str(self.join_cipher),offset=int(key))
                    print(cipher, "\t ", ord(cipher), "\t ", self.bin_to_8bit2,"\t",self.a28,"\t","XOR","\t","\t",self.a31,"\t","\t",chr(self.a31))
                print("\n")
                print("Plain Text:","\t",self.crack_caesar.decoded)


            if decion =="exit":
                exit()
            if decion =="help":
                print(self.banner2)

s=Securing_Caesar_Cipher()


 
 



