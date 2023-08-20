from django.db import models


class Payment(models.Model):
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = 'payments'
        # verb_osname = 'payment'
        # verb_osname_plural = 'payments'
    
    def __str__(self):
        return self.description





