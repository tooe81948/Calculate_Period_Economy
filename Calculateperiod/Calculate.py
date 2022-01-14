import math

class CalculatePeriodEconomy:
    
    def PE(self,output=1 , input=1 , percent=100 ): #ประสิทธิภาพเชิงฟิสิกส์ (Physical Efficiency)
        """ ประสิทธิภาพเชิงฟิสิกส์เป็นประสิทธิภาพเชิงกล เช่น เครื่องยนต์มีประสิทธิภาพ 80% โดยจะสูญเสีย 20%
            กับความร้อน ความเสียดทาน และอื่นๆเป็นต้น สามารถเขียนเป็นสมการได้ดังนี้

            PE = ( OUTPUT / INPUT ) x 100

            Output คือค่าที่ส่งออกมาหรือผลที่ได้รับ
            Input คือสิ่งที่ใช้ไป

            ประสิทธิภาพเชิงฟิสิกส์จะมีค่าไม่เกิน 100% เนื่องจากจะต้องมีการสูญเสียพลังงานไปกับสภาวะแวดล้อม
            ผลที่ได้รับจะน้อยกว่าสิ่งที่ใช้ไป """       
        return (output/input)*percent

    def EE(self,Worth=1 , Cost=1 , percent=100): #ประสิทธิภาพเชิงเศรษฐศาสตร์ (Economic Efficiency)
        """ ประสิทธิภาพเชิงเศรษฐศาสตร์มีสมการลักษณะเดียวกันกับประสิทธิภาพในเชิงฟิสิกส์ 
            แต่อยู่ในเทอมของมูลค่าของเงิน ซึ่งจะได้จากการนำเอามูลค่าของเงินที่ใช้ Worth หารด้วยมูลค่า
            ของเงินที่จ่าย Cost คูณด้วย 100

            EE = ( Worth / Cost ) x 100

            Worth คือมูลค่าของเงินที่ใช้
            Cost คือมูลค่าของเงินที่จ่าย

            ประสิทธิภาพเชิงเศรษฐศาสตร์นั้นมีค่าได้มากกว่า 100% 
            เพราะถ้าหากน้อยกว่า 100% ถือว่าโครงการนั้นขาดทุน """
        return (Worth/Cost)*percent

    def FIntR(self,Interest_rate=1 , times=1 ): #อัตตาดอกเบี้ยที่คิดมากกว่า 1 ครั้ง ใน 1 ปี
        """ เป็นอัตราดอกเบี้ยที่คิดบ่อยครั้ง
            Interest_rate ➔ อัตตราดอกเบี้ยที่คิด 1 ครั้งต่อปี หรือ 'r'
            times จำนวนครั้งที่คิดดอก หรือ จำนวนจ่ายแบบรายเดือน 'm'
            ผลลัพธ์ที่ออกมา คือ อัตตาดอกเบี้ยที่คิดมากกว่า 1 ครั้ง ใน 1 ปี
        """
        return ((1+((Interest_rate/100)/times))**times)-1

    def ContTRate(self,r=1): #อัตราดอกเบี้ยแบบต่อเนื่อง(continuous interest rate)
        """ r ➔ อัตตราดอกเบี้ยที่คิดครั้งหนึ่งใน 1 ปี
            ผลลัพธ์ที่ออกมา คือ อัตตราดอกเบี้ยที่คิดแบบต่อเนื่องใน 1 ปี
        """
        return (math.e**(r/100))-1

    def FtoP(self,Starting_value=1,percent=15,times=1): #จะเป็นการจ่ายงวดสุดท้ายเป็น เงินต้น + ดอกเบี้ย
        """ จะเป็นการจ่ายงวดสุดท้ายเป็น เงินต้น + ดอกเบี้ย

            Starting_value = มูลค่าเริ่มต้น (ต้นทุน) 'P'
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            (1 + i)n เรียกว่า Single Payment Compound Amount Factor (SPCAF)
            (1 + i)n สามารถใช้สัญลักษณ์แทนว่า (F/P, i%, n)

            ผลลัพธ์ที่ออกมาจะได้เป็น มูลค่าสุดท้าย (Final_value)
        """
        return Starting_value*(1+(percent/100))**times

    def PtoF(self,Final_value=1,percent=15,times=1):#มีอัตตราดอกเบี้ยและเงินสุดท้าย
        """ ระบบจ่ายครั้งเดียว (Single Payment System)
            หากเราต้องการทราบเงินเงินต้น โดยมีอัตตราดอกเบี้ยและเงินสุดท้าย

            Final_value = มูลค่าสุดท้าย
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            เรียกว่า Single Payment Present Worth Factor (SPPWF)
            สามารถใช้สัญลักษณ์แทนว่า (P/F, i%, n)

            ผลลัพธ์ที่ออกมาจะได้เป็น มูลค่าเริ่มต้น (ต้นทุน) (Starting_value)
        """
        return Final_value*(1/((1+(percent/100))**times))

    def PtoA(self,income=1,percent=15,times=1):
        """ ระบบการรับ-จ่ายแบบอนุกรมเท่าๆกันทุกช่วงเวลา
            เช่น การผ่อนชำระหนี้สอนจากการกู้ยืมเงินจากธนาคาร หรือ การฝากเงินทุกๆเดือนเท่าๆกัน
            ถ้าต้องผ่อนชำระเดือนละ A ต้องการจะหาวงเงินกู้ปัจจุบัน

            income = จำนวนเงินรายรับรายจ่ายเท่าๆกันทุกช่วงเวลา
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            เรียกว่า Uniform Series Present Worth Factors(USPWF)
            ใช้สัญลักษณ์ แทนว่า (P/A, i%, n)

            ผลลัพธ์ที่ออกมาจะได้เป็น มูลค่าเริ่มต้น (ต้นทุน) (Starting_value)
        """
        return (income*((((1+(percent/100))**times)-1)/((percent/100)*((1+(percent/100)**times)))))

    def AtoP(self,Starting_value=1,percent=15,times=1):
        """ ระบบการรับ-จ่ายแบบอนุกรมเท่าๆกันทุกช่วงเวลา
            ถ้ามีวงเงินปัจจุบัน และ ต้องการทราบเงินที่ต้องจ่ายแต่ละปี

            Starting_value = มูลค่าเริ่มต้น (ต้นทุน) 'P'
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            เรียกว่า Capital Recovery Factor (CRF)
            ใช้สัญลักษณ์ แทนว่า (A/P, i%, n)

            ผลลัพธ์ที่ออกมาจะได้เป็น จำนวนเงินรายรับรายจ่ายเท่าๆกันทุกช่วงเวลา(income)
        """
        return Starting_value*(((percent/100)*((1+(percent/100))**times)))/(((1+(percent/100))**times)-1)

    def AtoFtoP(self,Starting_value=1,percent=15,times=1):
        """ ระบบที่เพิ่มหรือลดสม่าเสมอ (Uniform Gradient System) 
            เช่นการประเมินค่าใช้จ่ายสำหรับซ่อมบำรุงเครื่องจักรซึ่งจะเพิ่มขึ้นทุกปี
            แต่ละปี ค่าใช้จ่ายเพิ่ม G ถ้าต้องการหามูลค่าเทียบเท่า F

            Starting_value = มูลค่าเริ่มต้น (ต้นทุน) 'P'
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            ผลลัพธ์ที่ออกมา คือ จำนวนเงินรายรับรายจ่ายเท่าๆกันทุกช่วงเวลา(income)
        """
        F = Starting_value*(1/((1+(percent/100))**times))
        return F*(((percent/100)*((1+(percent/100))**times)))/(((1+(percent/100))**times)-1)

    def PtoG(self,moneiup=1,percent=15,times=1):
        """ ระบบที่เพิ่มหรือลดสม่าเสมอ (Uniform Gradient System) 
            เช่นการประเมินค่าใช้จ่ายสำหรับซ่อมบำรุงเครื่องจักรซึ่งจะเพิ่มขึ้นทุกปี
            แต่ละปี ค่าใช้จ่ายเพิ่ม G ถ้าต้องการหามูลค่าเทียบเท่า F
        
            moneiup = ค่าเฉพาะส่วนที่เพิ่มในแต่ละปี 'G'
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            เรียกว่า Uniform Gradient Present Worth Factor (UGPWF)
            สามารถแทนได้ด้วยสัญลักษณ์ (P/G, i%, n)

            ผลลัพธ์ที่ออกมา คือ มูลค่าเริ่มต้น (ต้นทุน) (Starting_value)
        """
        G = moneiup/(percent/100) #ค่าเฉพาะส่วนที่เพิ่มในแต่ละปี
        n1 = ((((1+(percent/100))**times)-1)/((percent/100)*((1+(percent/100)**times))))
        n2 = times/((1+(percent/100))**times)
        return G*(n1-n2)

    def FtoG(self,moneiup=1,percent=15,times=1):
        """ ระบบที่เพิ่มหรือลดสม่าเสมอ (Uniform Gradient System)
            เช่นการประเมินค่าใช้จ่ายส าหรับซ่อมบ ารุงเครื่องจักรซึ่งจะเพิ่มขึ้นทุกปี
            แต่ละปี ค่าใช้จ่ายเพิ่ม G ถ้าต้องการหามูลค่าเทียบเท่า (F)

            moneiup = ค่าเฉพาะส่วนที่เพิ่มในแต่ละปี 'G'
            percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
            times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'

            ผลที่ได้ที่ออกมา คือ มูลค่าสุดท้าย (Final_value)
        """
        G = moneiup/(percent/100)
        n1 = (((1+(percent/100))**times)-1)/(percent/100)
        n2 = (times*moneiup)/(percent/100)
        return G*(n1-n2)
    
    def help(self):
        Data = """แนะนำวิธีการใช้งาน Calculate_period

    **PE คือ ประสิทธิภาพเชิงฟิสิกส์เป็นประสิทธิภาพเชิงกล เช่น เครื่องยนต์มีประสิทธิภาพ 80% โดยจะสูญเสีย 20%
        จะรับ Input เป็น  
            Output ➔ ค่าที่ส่งออกมาหรือผลที่ได้รับ
            Input ➔ สิ่งที่ใช้ไป
            percent ➔ เปอร์เซ็น

        ค่า Output จะมีค่าน้อยกว่า Input เสมอ
    ตัวอย่าง PE( Output=94 , Input=100 , percent=100 )


    **EE คือ ประสิทธิภาพเชิงเศรษฐศาสตร์มีสมการลักษณะเดียวกันกับประสิทธิภาพในเชิงฟิสิกส์ 
        จะรับ Input เป็น 
            Worth ➔ มูลค่าของเงินที่ใช้
            Cost ➔ มูลค่าของเงินที่จ่าย
            percent ➔ เปอร์เซ็น

        ประสิทธิภาพเชิงเศรษฐศาสตร์นั้นมีค่าได้มากกว่า 100% เพราะถ้าหากน้อยกว่า 100% ถือว่าโครงการนั้นขาดทุน
    ตัวอย่าง EE( Worth=300000 , Cost=250000 , percent=100 )


    **FIntR คือ เป็นอัตราดอกเบี้ยที่คิดบ่อยครั้ง
        จะรับ Input เป็น 
            Interest_rate ➔ อัตตราดอกเบี้ยที่คิด 1 ครั้งต่อปี หรือ 'r'
            times ➔ จำนวนครั้งที่คิดดอก หรือ จำนวนจ่ายแบบรายเดือน 'm'
    ตัวอย่าง FIntR( Interest_rate=15 , times=12 )


    **ContTRate คือ อัตราดอกเบี้ยแบบต่อเนื่อง
        r ➔ อัตตราดอกเบี้ยที่คิดครั้งหนึ่งใน 1 ปี
    ตัวอย่าง ContTRate( r=12 )   


    **FtoP คือ จะเป็นการจ่ายงวดสุดท้ายเป็น เงินต้น + ดอกเบี้ย
        Starting_value ➔ มูลค่าเริ่มต้น (ต้นทุน) 'P'
        percent ➔ อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times ➔ ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง FtoP(Starting_value=100000,percent=15,times=5)


    **PtoF คือ ระบบจ่ายครั้งเดียว (Single Payment System)
                หากเราต้องการทราบเงินเงินต้น โดยมีอัตตราดอกเบี้ยและเงินสุดท้าย
        Final_value = มูลค่าสุดท้าย
        percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง PtoF(Final_value=50000,percent=10,times=3)


    **PtoA คือ ระบบการรับ-จ่ายแบบอนุกรมเท่าๆกันทุกช่วงเวลา
                เช่น การผ่อนชำระหนี้สอนจากการกู้ยืมเงินจากธนาคาร หรือ การฝากเงินทุกๆเดือนเท่าๆกัน
                ถ้าต้องผ่อนชำระเดือนละ A ต้องการจะหาวงเงินกู้ปัจจุบัน
        income = จำนวนเงินรายรับรายจ่ายเท่าๆกันทุกช่วงเวลา
        percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง PtoA(income=5200,percent=15,times=7)


    **AtoP คือ ระบบการรับ-จ่ายแบบอนุกรมเท่าๆกันทุกช่วงเวลา
                ถ้ามีวงเงินปัจจุบัน และ ต้องการทราบเงินที่ต้องจ่ายแต่ละปี
        Starting_value = มูลค่าเริ่มต้น (ต้นทุน) 'P'
        percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง AtoP(Starting_value=520000,percent=15,times=7)


    **AtoFtoP คือ ระบบที่เพิ่มหรือลดสม่าเสมอ (Uniform Gradient System) 
                    เช่นการประเมินค่าใช้จ่ายสำหรับซ่อมบำรุงเครื่องจักรซึ่งจะเพิ่มขึ้นทุกปี
                    แต่ละปี ค่าใช้จ่ายเพิ่ม G ถ้าต้องการหามูลค่าเทียบเท่า F
        Starting_value = มูลค่าเริ่มต้น (ต้นทุน) 'P'
        percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง AtoFtoP(Starting_value=30000,percent=12,times=2)


    **PtoG คือ ระบบที่เพิ่มหรือลดสม่าเสมอ (Uniform Gradient System) 
                เช่นการประเมินค่าใช้จ่ายสำหรับซ่อมบำรุงเครื่องจักรซึ่งจะเพิ่มขึ้นทุกปี
                แต่ละปี ค่าใช้จ่ายเพิ่ม G ถ้าต้องการหามูลค่าเทียบเท่า F
        moneiup = ค่าเฉพาะส่วนที่เพิ่มในแต่ละปี 'G'
        percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง PtoG(moneiup=2000,percent=10,times=12)


    **FtoG คือ ระบบที่เพิ่มหรือลดสม่าเสมอ (Uniform Gradient System)
                เช่นการประเมินค่าใช้จ่ายส าหรับซ่อมบ ารุงเครื่องจักรซึ่งจะเพิ่มขึ้นทุกปี
                แต่ละปี ค่าใช้จ่ายเพิ่ม G ถ้าต้องการหามูลค่าเทียบเท่า (F)
        moneiup = ค่าเฉพาะส่วนที่เพิ่มในแต่ละปี 'G'
        percent = อัตราดอกเบี้ยต่อระยะเวลา หรือ 'i'
        times = ระยะเวลาหรือช่วงเวลา เช่น วัน เดือน ปี หรือ 'n'
    ตัวอย่าง PtoG(moneiup=1200,percent=0,times=20)

        """
        print(Data)