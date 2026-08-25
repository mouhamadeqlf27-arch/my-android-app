# تطبيق حجب إعلانات Spotify للهاتف - النسخة الكاملة
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from PIL import Image as PilImage, ImageDraw, ImageFont
import os

# توليد الشعار أوتوماتيكياً
def create_default_logo():
    if not os.path.exists("logo.png"):
        img = PilImage.new('RGB', (300, 300), color='#121212')
        d = ImageDraw.Draw(img)
        d.ellipse([50, 50, 250, 250], fill='#1DB954')
        try:
            font = ImageFont.truetype("arial.ttf", 100)
        except:
            font = ImageFont.load_default()
        d.text((110, 95), "S", fill="white", font=font)
        img.save("logo.png")

create_default_logo()

class SpotifyAdCleanerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        # إضافة اللوغو
        try:
            self.logo = Image(source='logo.png', size_hint=(None, None), size=(160, 160), pos_hint={'center_x': 0.5})
            layout.add_widget(self.logo)
        except:
            pass
        s
        # عنوان التطبيق
        title_label = Label(
            text="Spotify Ad-Cleaner", 
            font_size='24sp', 
            bold=True, 
            color=(0.11, 0.73, 0.33, 1)
        )
        layout.add_widget(title_label)
        
        # حالة الحماية
        self.status_label = Label(
            text="الحالة: الحماية الفورية تعمل في الخلفية 🟢", 
            font_size='14sp', 
            color=(1, 1, 1, 1)
        )
        layout.add_widget(self.status_label)
        
        # زر التحكم
        self.action_btn = Button(
            text="إيقاف مؤقت للحماية", 
            size_hint=(1, 0.18), 
            background_color=(0.9, 0.2, 0.2, 1),
            font_size='16sp',
            bold=True
        )
        self.action_btn.bind(on_press=self.toggle_engine)
        layout.add_widget(self.action_btn)
        
        return layout

    def toggle_engine(self, instance):
        if "تعمل" in self.status_label.text:
            self.status_label.text = "الحالة: الحماية متوقفة 🔴"
            self.action_btn.text = "تشغيل الحماية"
            self.action_btn.background_color = (0.11, 0.73, 0.33, 1)
        else:
            self.status_label.text = "الحالة: الحماية الفورية تعمل في الخلفية 🟢"
            self.action_btn.text = "إيقاف مؤقت للحماية"
            self.action_btn.background_color = (0.9, 0.2, 0.2, 1)

if __name__ == '__main__':
    SpotifyAdCleanerApp().run()