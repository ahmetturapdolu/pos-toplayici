from decimal import Decimal
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Ekran(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.genel_toplam = Decimal("0.00")
        self.siradaki_tutar = Decimal("125.50")  # Test için şimdilik sabit bir tutar

        # --- ÜST YARI ---
        ust_alan = BoxLayout(orientation="vertical", size_hint_y=0.5)
        self.flas_buton = Button(text="Flaş: Kapalı", size_hint_y=None, height="45dp")
        self.flas_buton.bind(on_press=self.flas_degistir)

        kamera_alani = Label(text="ÜST YARI\n(Buraya canlı kamera gelecek)")

        ust_alan.add_widget(self.flas_buton)
        ust_alan.add_widget(kamera_alani)

        # --- ALT YARI ---
        alt_alan = BoxLayout(orientation="vertical", size_hint_y=0.5, padding="10dp", spacing="6dp")

        self.soru_etiketi = Label(
            text=f"Tutar Doğru mu?  {self.siradaki_tutar}",
            size_hint_y=None,
            height="36dp",
        )
        alt_alan.add_widget(self.soru_etiketi)

        buton_satiri = BoxLayout(size_hint_y=None, height="48dp", spacing="10dp")
        evet_buton = Button(text="Evet")
        hayir_buton = Button(text="Hayır")
        evet_buton.bind(on_press=self.evet_tiklandi)
        hayir_buton.bind(on_press=self.hayir_tiklandi)
        buton_satiri.add_widget(evet_buton)
        buton_satiri.add_widget(hayir_buton)
        alt_alan.add_widget(buton_satiri)

        kaydirma = ScrollView()
        self.liste_kutusu = GridLayout(cols=1, size_hint_y=None, spacing="4dp")
        self.liste_kutusu.bind(minimum_height=self.liste_kutusu.setter("height"))
        kaydirma.add_widget(self.liste_kutusu)
        alt_alan.add_widget(kaydirma)

        self.toplam_etiketi = Label(
            text="Genel Toplam: 0.00",
            size_hint_y=None,
            height="40dp",
        )
        alt_alan.add_widget(self.toplam_etiketi)

        self.add_widget(ust_alan)
        self.add_widget(alt_alan)

    def flas_degistir(self, _instance):
        if self.flas_buton.text == "Flaş: Kapalı":
            self.flas_buton.text = "Flaş: Açık"
        else:
            self.flas_buton.text = "Flaş: Kapalı"

    def evet_tiklandi(self, _instance):
        satir = Label(text=f"{self.siradaki_tutar}  +", size_hint_y=None, height="28dp")
        self.liste_kutusu.add_widget(satir)

        self.genel_toplam += self.siradaki_tutar
        self.toplam_etiketi.text = f"Genel Toplam: {self.genel_toplam}"

    def hayir_tiklandi(self, _instance):
        # Hayır denildiğinde hiçbir şey eklenmez
        pass


class PosApp(App):
    def build(self):
        return Ekran()


if __name__ == "__main__":
    PosApp().run()