# ini adalah aplikasi kalkulator microstrip

import math
import sys
from PyQt5.QtWidgets import QDialog,QApplication
from guikalku import *  


def cutoffFreq(c, er, w, h):
    Fc = c/(math.sqrt(er)*(2*w+0.8*h))
    return Fc

def Eeffektif(er, h, w):
    if (w/h) <= 1:
        ere = ((er+1)/2)+((er-1)/2)*(1/(math.sqrt(1+12*(h/w))))+0.04*(1-((w/h)**2))
        return ere
    elif (w/h) > 1:
        ere = ((er+1)/2)+((er-1)/2)*(1/(math.sqrt(1+12*(h/w))))
        return ere
    else:
        return 0

#def kapasitansi(w,h):
    

def guidedWavelength(f, eeff):
    Lamg = 300/(f*math.sqrt(eeff))
    return Lamg

def konstanPropagasi(panjgelguid):
    beta = (2*math.pi)/panjgelguid
    return beta

def panjElektris(beta, l):
    tetaa = beta*l
    return tetaa
    
def panjGelruangHampa(f):
    c = 3*(10**8)
    lamd0 = c/f
    return lamd0

def impendansi(eeff, h, w):
    if w/h <1:
        zo = (60/(math.sqrt(eeff)))*math.log((8*(h/w))+(0.25*(w/h)))
        return zo
    else:
        zo = (math.pi*120)/(math.sqrt(eeff)*((w/h)+1.393+0.666666666666*math.log((w/h)+1.444)))
        return zo

def impendanGel(er): 
    n = 376.73/math.sqrt(er)
    return n

def panjang(lamdag):
    l = lamdag/4
    return l



class keluaran(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.hitung.clicked.connect(self.hitung)
        self.ui.reset.clicked.connect(self.hilang)
        self.show()
        # set the title
        self.setWindowTitle("Aplikasi Mikrostrip Sederhana Buatan Kelompok 2")
 
    
    def hitung(self):
        try: 
            h = float(self.ui.ketebalan.text())
            w = float(self.ui.panjang.text())
            er = float(self.ui.permitivitas.text())
            f = float(self.ui.frekuensi.text())
        except ValueError:
           self.ui.errormsg.setText("MASUKKAN ANGKA JANGAN HURUF APALAGI KARAKTER!")
           self.ui.ketebalan.setText(str())
           self.ui.panjang.setText(str())
           self.ui.permitivitas.setText(str())
           self.ui.frekuensi.clear()
        
        else:
            conduct = 59.6*(10**6)

            fc = cutoffFreq(conduct, er, w, h)
            Eeff = Eeffektif(er, h, w)
            guidedPanjGel = guidedWavelength(f, Eeff)
            beta = konstanPropagasi(guidedPanjGel)
            l = panjang(guidedPanjGel)
            teta = panjElektris(beta, l)
            lamda0 = panjGelruangHampa(fc)
            zo = impendansi(Eeff, h, w)
            n = impendanGel(er)

            self.ui.panjangl.setText(str(round(l, 4)))
            self.ui.fcutoff.setText(str(round(fc, 4)))
            self.ui.zo.setText(str(round(zo,4)))
            self.ui.zo_2.setText(str(round(n, 4)))
            self.ui.eeff.setText(str(round(Eeff, 4)))
            self.ui.guidedWave.setText(str(round(guidedPanjGel,4)))
            self.ui.panjangGel.setText(str(round(lamda0,4)))
            self.ui.konsPropagasi.setText(str(round(beta,4)))
            self.ui.panjangel.setText(str(round(teta,4)))
            self.ui.errormsg.clear()

    def hilang(self):
        self.ui.panjangl.clear()
        self.ui.fcutoff.clear()
        self.ui.zo.clear()
        self.ui.zo_2.clear()
        self.ui.eeff.clear()
        self.ui.guidedWave.clear()
        self.ui.panjangGel.clear()
        self.ui.konsPropagasi.clear()
        self.ui.panjangel.clear()
        self.ui.ketebalan.clear()
        self.ui.panjang.clear()
        self.ui.permitivitas.clear()
        self.ui.frekuensi.clear()
        self.ui.errormsg.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = keluaran()
    w.show()
    sys.exit(app.exec_())








#bagian keluaran

