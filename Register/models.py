
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

class Register(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Age = models.IntegerField()
    PhoneNum = models.CharField(max_length=50)
    Designation = models.CharField(max_length=500)
    Photo = models.ImageField(upload_to='Register_photos/', null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return self.Name

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Data to encode in QR code
        data = f"Name: {self.Name}, Email: {self.Email}, Age: {self.Age}, PhoneNum: {self.PhoneNum}, Designation: {self.Designation}"
        qr.add_data(data)
        qr.make(fit=True)

        # Create an in-memory stream to save the image
        qr_code_img = qr.make_image(fill_color="black", back_color="white")
        stream = BytesIO()
        qr_code_img.save(stream, format='PNG')
        stream.seek(0)

        # Assign the image to the QR code field
        self.qr_code.save(f'{self.Name}_qr.png', File(stream), save=True)
