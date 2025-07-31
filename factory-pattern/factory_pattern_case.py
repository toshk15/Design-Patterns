class Fly:
    def shoot(self):
        pass

class Banshee(Fly):
    def shoot(self):
        print("Banshee shoots a missile")

class B747Fly(Fly):
    def shoot(self):
        print("B747 shoots a water cannon")
    
class A380Fly(Fly):
    def shoot(self):
        print("A380 shoots a water cannon")

class FlyFactory:
    @staticmethod
    def create(type):
        if type == 0:
            return Banshee()
        elif type == 1:
            return B747Fly()
        elif type == 2:
            return A380Fly()
        else:
            return None

p = FlyFactory.create(0)
p.shoot()