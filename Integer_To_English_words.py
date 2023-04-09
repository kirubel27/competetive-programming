class Solution:
    def numberToWords(self, num: int) -> str:
        if num ==0:
            return "Zero"
        U_20 = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight","Nine", "Ten", "Eleven","Twelve", "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty"]
        F10_100=["","Ten", "Twenty", "Thirty", "Forty","Fifty","Sixty","Seventy","Eighty","Ninety","Hundred"]
        def rec(num:int)-> str:
            if num<=20:
                res =  U_20[num]
            elif num==30 or num== 40 or num==50 or num ==60 or num==70 or num==80 or num==90:
                res= F10_100[num//10]
            elif num<100  :
                res = F10_100[num//10] + " " + U_20[num%10]
            elif num<1000:
                res= U_20[num//100] + " Hundred " + rec(num%100)
            elif num<1000000:
                res = rec(num//1000) +" Thousand " + rec(num%1000)
            elif num<1000000000:
                res = rec(num//1000000) + " Million " + rec(num%1000000)
            else:
                res= rec(num//1000000000) + " Billion " + rec(num%1000000000)
            return res.strip()
        return rec(num)
