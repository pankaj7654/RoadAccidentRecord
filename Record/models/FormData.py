from django.db import models


class RecordFormData(models.Model):
    fireno = models.CharField(max_length = 50)
    ipc = models.CharField(max_length = 50)
    # dateoffence = models.DateTimeField(null=False, auto_now_add=True)
    # dateoffencefir = models.DateTimeField(null=False, auto_now_add=True)
    # day = models.DateTimeField(null=False, auto_now_add=True)
    # Timeoffence = models.DateTimeField(null=False, auto_now_add=True)

    # district = (
    #     ('green','GREEN'),
    #     ('blue', 'BLUE'),
    #     ('red','RED'),
    #     ('orange','ORANGE'),
    #     ('black','BLACK'),
    # )
    # district = models.CharField(max_length=50, choices=district)
    # policestation = models.CharField(max_length = 50)
    # firstvehicle = models.CharField(max_length = 50, choices=firstvehicle)
    # Nooffatalties = models.CharField(max_length = 50)
    # seriousinjured = models.CharField(max_length = 50)
    # minorinjured = models.CharField(max_length = 50)
    # secondvehicle = models.CharField(max_length = 50, choices=secondvehicle)
    # Nooffatalties2 = models.CharField(max_length = 50)
    # seriousinjured2 = models.CharField(max_length = 50)
    # minorinjured2 = models.CharField(max_length = 50)
    # maneuvertype = models.CharField(max_length = 50, choices=maneuvertype)
    # location = models.CharField(max_length = 50)
    # typeofcollision = models.CharField(max_length = 50, choices=typeofcollision)
    # hitandrun = models.CharField(max_length = 50, choices=typeofcollision)

    # roadname = models.CharField(max_length = 50)
    # roadnumber = models.CharField(max_length = 50)
    # landmark = models.CharField(max_length = 50)
    # roadcategory = models.CharField(max_length = 50, choices=roadcategory)
    # roadtype = models.CharField(max_length = 50, choices=roadtype)
    # midblock = models.CharField(max_length = 50, choices=midblock)
    # junctiontype = models.CharField(max_length = 50, choices=junctiontype)
    # ruralurban = models.CharField(max_length = 50, choices=ruralurban)
    # medical = models.CharField(max_length = 50, choices=medical)
    # longitude = models.CharField(max_length = 50)
    # latitude = models.CharField(max_length = 50)

    # totalfatalities = models.CharField(max_length = 50)
    # totalsrlyinjuries = models.CharField(max_length = 50)
    # totalminorinjuries = models.CharField(max_length = 50)
    # malefatalities = models.CharField(max_length = 50)
    # femalefatalities = models.CharField(max_length = 50)
    # lesseighteenmale = models.CharField(max_length = 50)
    # lesseighteenfemale = models.CharField(max_length = 50)
    # eighteentotwentyfivemale = models.CharField(max_length = 50)
    # eighteentotwentyfivefemale = models.CharField(max_length = 50)
    # twentyfivetofourtyfivemale = models.CharField(max_length = 50)
    # twentyfivetofourtyfivefemale = models.CharField(max_length = 50)
    # fourtyfivetosixtymale = models.CharField(max_length = 50)
    # fourtyfivetosixtyfemale = models.CharField(max_length = 50)
    # abovesixtymale = models.CharField(max_length = 50)
    # abovesixtyfemale = models.CharField(max_length = 50)
    # agenotknownmale = models.CharField(max_length = 50)
    # agenotknownfemale = models.CharField(max_length = 50)
    # remarks = models.CharField(max_length = 1000)
  