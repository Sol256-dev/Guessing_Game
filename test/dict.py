class Phone:

    net_band = '4G'

    def __init__(self, camera, size, simcards):
        self.camera = camera
        self.size = size
        self.simcards = simcards

    def phn_sel(self):
        mob_phn = {
            'Nokia': 'has a ' + self.camera + 'mp camera',
            'Samsung': 'has a ' + self.camera + 'mp camera',
            'Motorolla': 'has a ' + self.camera + 'mp camera'
        }

        return list(mob_phn)
