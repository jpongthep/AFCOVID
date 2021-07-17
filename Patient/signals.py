from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

from Patient.models import Patient, StatusLog, TreatmentLog


@receiver(post_save, sender=StatusLog)
def PostSaveSignal(sender, instance, **kwargs):
    LastestStatus = StatusLog.objects.filter(ThePatient = instance.ThePatient).order_by('-Date')
    if LastestStatus.exists():
        StatusResult =  LastestStatus[0].Status
    else:
        StatusResult = 0
    
    patient = Patient.objects.get(id = instance.ThePatient.id)
    patient.CurrentStatus = StatusResult
    patient.save()

@receiver(post_save, sender=TreatmentLog)
def PostSaveSignal(sender, instance, **kwargs):
    LastestTreatment = TreatmentLog.objects.filter(ThePatient = instance.ThePatient).order_by('-Date')
    if LastestTreatment.exists():
        TreatmentResult =  LastestTreatment[0].Treatment
    else:
        TreatmentResult = 0
    
    patient = Patient.objects.get(id = instance.ThePatient.id)
    patient.CurrentTreatment = TreatmentResult
    patient.save()


# pre_save.connect(PreSaveSignal, sender=LeaveData)
post_save.connect(PostSaveSignal, sender=StatusLog)
post_save.connect(PostSaveSignal, sender=TreatmentLog)
# pre_delete.connect(PreDeleteSignal, sender=LeaveData)
# post_delete.connect(PostDeleteSignal, sender=LeaveData)