class Plug:
    def recharge(self):
        pass

class HighVoltagePlug(Plug):
    def recharge(self):
        return 100

class AdapterPlug(Plug):
    def recharge(self):
        high_plug = HighVoltagePlug()
        high_voltage = high_plug.recharge()
        low_voltage = high_voltage - 64
        return low_voltage
    
plug = HighVoltagePlug()
print(plug.recharge())

plug = AdapterPlug()
print(plug.recharge())