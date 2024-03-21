from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WorkType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AcademicLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# class Work(models.Model):
#     name = models.CharField(max_length=50)
#     words = models.IntegerField(default=0)
#     pages = models.IntegerField(default=1)
#     work_type = models.ForeignKey('core.WorkType', related_name='works', on_delete=models.CASCADE)
#     paper_format = models.CharField(max_length=50, null=True, blank=True)
#     academic_level = models.ForeignKey('core.AcademicLevel', related_name='works', on_delete=models.CASCADE)
#     sources_needed = models.CharField(max_length=50, null=True, blank=True)
#     preferred_language_style = models.CharField(max_length=50, null=True, blank=True)
#     files = models.ForeignKey('core.OrderFile', related_name='works', on_delete=models.CASCADE, null=True, blank=True)
#     topic = models.CharField(max_length=255, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
    ('broadcast', 'Broadcast'),
)

class Order(models.Model):
    order_id = models.CharField(max_length=50)
    subject = models.ForeignKey('core.Subject', related_name='orders', on_delete=models.CASCADE)
    work = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deadline = models.DateTimeField(null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default='pending', choices=STATUS_CHOICES)
    writer = models.ForeignKey('accounts.User', related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    academic_level = models.ForeignKey('core.AcademicLevel', related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    words = models.IntegerField(default=0)
    pages = models.IntegerField(default=1)
    work_type = models.ForeignKey('core.WorkType', related_name='works', on_delete=models.CASCADE)
    paper_format = models.CharField(max_length=50, null=True, blank=True)
    academic_level = models.ForeignKey('core.AcademicLevel', related_name='works', on_delete=models.CASCADE)
    sources_needed = models.CharField(max_length=50, null=True, blank=True)
    preferred_language_style = models.CharField(max_length=50, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.order_id


class OrderMessage(models.Model):
    order = models.ForeignKey('core.Order', related_name='order_messages', on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.ForeignKey('accounts.User', related_name='order_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey('accounts.User', related_name='order_messages_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['created_at']


class OrderFile(models.Model):
    order = models.ForeignKey('core.Order', related_name='order_files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    creator = models.ForeignKey('accounts.User', related_name='order_files', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order)
