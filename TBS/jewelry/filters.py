import django_filters
from jewelry.models import Merchandise,PriceCategory,Jewel
from django import forms

class MerchandiseFilterBase(django_filters.FilterSet):
	price_category = django_filters.ModelMultipleChoiceFilter(
		queryset=PriceCategory.objects.all(),
		widget=forms.CheckboxSelectMultiple(),
	)
	#start_date = django_filters.DateFilter(field_name='created',lookup_expr=('gt'),) 
	#end_date = django_filters.DateFilter(field_name='created',lookup_expr=('lt'))
	#date_range = django_filters.DateFromToRangeFilter(field_name='created')
	created = django_filters.DateFromToRangeFilter(
		widget=forms.SplitDateTimeWidget(
			attrs={
				'class':'datepicker',
				'type':'date',
			}
		)
	)


class MerchandiseFilter(MerchandiseFilterBase):
    merchandise_type = django_filters.MultipleChoiceFilter(
    	choices=Merchandise.MERCHANDISE_TYPE,
    	widget=forms.CheckboxSelectMultiple(),
    )
    
    class Meta:
        model = Merchandise
        fields = ['merchandise_type','price_category','created']


class JewelFilter(MerchandiseFilterBase):
	jewel_type = django_filters.MultipleChoiceFilter(
		choices = Jewel.JEWEL_TYPE,
		widget=forms.CheckboxSelectMultiple(),
	)
	class Meta:
		model = Jewel
		fields = ['price_category','created','jewel_type']