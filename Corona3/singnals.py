# from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
# from django.dispatch import receiver

# from Corona3.models import Corona3
# , StatusLog, TreatmentLog


# @receiver(post_save, sender=StatusLog)
# def PostSaveSignal(sender, instance, **kwargs):
#     LastestStatus = StatusLog.objects.filter(TheCorona3 = instance.TheCorona3).order_by('-Date')
#     if LastestStatus.exists():
#         StatusResult =  LastestStatus[0].Status
#     else:
#         StatusResult = 0
    
#     Corona3 = Corona3.objects.get(id = instance.TheCorona3.id)
#     Corona3.CurrentStatus = StatusResult
#     Corona3.save()

# @receiver(post_save, sender=TreatmentLog)
# def PostSaveSignal(sender, instance, **kwargs):
#     LastestTreatment = TreatmentLog.objects.filter(TheCorona3 = instance.TheCorona3).order_by('-Date')
#     if LastestTreatment.exists():
#         TreatmentResult =  LastestTreatment[0].Treatment
#     else:
#         TreatmentResult = 0
    
#     Corona3 = Corona3.objects.get(id = instance.TheCorona3.id)
#     Corona3.CurrentTreatment = TreatmentResult
#     Corona3.save()


# pre_save.connect(PreSaveSignal, sender=DonorData)
# post_save.connect(PostSaveSignal, sender=StatusLog)
# post_save.connect(PostSaveSignal, sender=TreatmentLog)
# pre_delete.connect(PreDeleteSignal, sender=DonorData)
# post_delete.connect(PostDeleteSignal, sender=DonorData)