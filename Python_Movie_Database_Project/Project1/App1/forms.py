from django import forms
from .models import MovieRecord

Vaccine_list=(('CoVaccine','Covaccine'),('Covishield','Covishield'))
Hos_list=(('Jahangir Hospital','Jahangir Hospital'),('Ruby Hall Clinic','Ruby Hall Clinic'),('Sahyadri Hospital','Sahyadri Hospital'),('Sancheti Hospital','Sancheti Hospital'))


class MovieRecordForm(forms.ModelForm):
    class Meta:
        model=MovieRecord
        fields='__all__'
        labels={
        'Movie_Name':'Enter Movie Name',
        'Release_date':'Select Release  date',
        'Movie_starcast':'Enter  starcast Name',
        'Movie_Director': 'Enter Movie_Director Name',
        'Movie_poster':'upload Poster'}

        widgets={
        'Release_date':forms.NumberInput(attrs={'type':'date'})}