from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Simular dimensiones de pantalla de celular (opcional para desarrollo)
Window.size = (360, 640)

class SimuladorApp(App):
    def build(self):
        # Contenedor vertical con padding y espaciado
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Título
        layout.add_widget(Label(text='Cálculo de Velocidad Media', font_size=20, bold=True, size_hint_y=None, height=40))

        # Campo: Distancia
        layout.add_widget(Label(text='Distancia (m):', size_hint_y=None, height=30))
        self.input_d = TextInput(multiline=False, input_filter='float', size_hint_y=None, height=40)
        layout.add_widget(self.input_d)

        # Campo: Tiempo
        layout.add_widget(Label(text='Tiempo (s):', size_hint_y=None, height=30))
        self.input_t = TextInput(multiline=False, input_filter='float', size_hint_y=None, height=40)
        layout.add_widget(self.input_t)

        # Botón de cálculo
        btn = Button(text='Calcular', size_hint_y=None, height=50, background_color=(0.2, 0.6, 1, 1))
        btn.bind(on_press=self.calcular)
        layout.add_widget(btn)

        # Etiqueta de resultado
        self.lbl_resultado = Label(text='Resultado: -- m/s', font_size=18, bold=True)
        layout.add_widget(self.lbl_resultado)

        return layout

    def calcular(self, instance):
        try:
            d = float(self.input_d.text)
            t = float(self.input_t.text)
            if t != 0:
                v = d / t
                self.lbl_resultado.text = f'Resultado: {v:.2f} m/s'
            else:
                self.lbl_resultado.text = 'El tiempo no puede ser cero'
        except ValueError:
            self.lbl_resultado.text = 'Ingresa valores válidos'

if __name__ == '__main__':
    SimuladorApp().run()
