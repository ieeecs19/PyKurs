import random
import re
#1-4 sayı al , 1-13 sayı al bunlara bi kart 
#random.shuffle
def masayıyazdır(x) : 
  if (x=="Oyuncu") : 
    print()
    print("----------------------------------------")
    print(kurpiyer[0])
    print("-------Blackjack Gives 3 to 1 ----------")
    for x in oyuncu : 
        print(x ,"|", end=" ")
    print()
    print("----------------------------------------")     
  else:  
    print()
    print("----------------------------------------")
    for x in kurpiyer : 
        print(x ,"|", end=" ") 
    print()
    print("-------Blackjack Gives 3 to 1 ----------")
    for x in oyuncu : 
        print(x ,"|", end=" ") 
    print()
    print("----------------------------------------")    

para=100
while(1):
  deste = []
  for c in range(1,14):
      
    deste.append("Kupa "+str(c))
    deste.append("Karo "+str(c))
    deste.append("Maça "+str(c))
    deste.append("Sinek "+str(c))


  destex2 = deste*2
  random.shuffle(destex2)
  
  kurpiyer =[]
  oyuncu=[]

  
  kurpiyer.append(destex2.pop())
  masayıyazdır("Oyuncu")
  if(para>0):
    bahiskarar=input("Oyuna gir yada çık (e/h)")
    if (bahiskarar== "e") :
    
      bahismiktar = int(input("bahis miktarı nedir ?"+ str(para)+"  "))
      if(bahismiktar>para):
        while(bahismiktar>para):
          print("bahsiniz para miktarınızdan büyüktür.Tekrar bahis giriniz.para = "+str(para)+"  ")
          bahismiktar = int(input())
      para = para-bahismiktar
      kurpiyer.append(destex2.pop())

      oyuncu.append(destex2.pop())
      Opuan =0
      Opuan2 = 0
      flagLose = False
      flagBlackjack = False
      flagwin = False
      Devam="e"
      #oyuncuya kart isteyip istemediğini sor
      while(Devam =="e") : 
        oyuncu.append(destex2.pop())
        masayıyazdır("Oyuncu")
        Opuan = 0
        Opuan2 = 0
        for x in oyuncu :
          if(int(re.search(r'\d+', x).group()) > 10) : 
            Opuan=Opuan+10
            
          elif(int(re.search(r'\d+', x).group())== 1):
            Opuan=Opuan+1
            Opuan2 = Opuan2+ 10
            
          else : 
            Opuan = Opuan + int(re.search(r'\d+', x).group())
            
        print()
        print("puanınız : " + str(Opuan))
        if(Opuan2 != 0 ) : 
          if(Opuan+Opuan2 <= 21):
            print("As 11 olarak olursa : "+str(Opuan+Opuan2))
            Opuan2=Opuan+Opuan2
        if(Opuan >21):
          print("kaybettiniz.")
          flagLose = True
          break
        if(Opuan2==21  or Opuan == 21) : 
          print("Blackjack !")
          flagBlackjack =True
          break
        Devam = input("Kart istermisiniz ?(e/h)")
      Kpuan = 0
      Kpuan2 = 0
      if(flagBlackjack == False and flagLose == False) : 
        print("kurpiyer Oynuyor.")
        
        while(Kpuan<=16 or Kpuan2<=16):
          masayıyazdır("Kurpiyer")
          Kpuan= 0
          Kpuan2= 0
          for x in kurpiyer :
            if(int(re.search(r'\d+', x).group()) > 10) : 
              Kpuan=Kpuan+10
              
            elif(int(re.search(r'\d+', x).group())== 1):
              Kpuan=Kpuan+1
              Kpuan2 = Kpuan2+ 10
            else : 
              Kpuan = Kpuan + int(re.search(r'\d+', x).group())
          if(Kpuan>16 or Kpuan2>16) : 
            break
          if(Kpuan==21 or Kpuan2==21):
            print("kurpiyer kazandı")
            flagLose = True
            break
          if(Kpuan>21) : 
            print("Kurpiyer battı.")
            flagwin = True
            break
          kurpiyer.append(destex2.pop())
       
      if(Opuan > Kpuan or Opuan2>Kpuan or Opuan2>Kpuan2 or Opuan>Kpuan2) : 
            flagwin = True
        
      if(flagBlackjack == True) : 
        para = para + bahismiktar *3
          
      if(flagwin == True) : 
        para = para + bahismiktar*2

      print("Para Miktarınız : ",para)
      if(para == 0 ):
        print("paranız bitmiştir! Oyun sonlandı.")
        
  
