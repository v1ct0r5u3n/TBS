import django_filters
from jewelry.models import Merchandise,PriceCategory,Jewel,Accessory,Pearl,Diamond,ColoredGem
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

class OtherFilter(MerchandiseFilterBase):
	@property
	def qs(self):
		parent = super().qs
		return parent.filter(merchandise_type='') 
	class Meta:
		model = Merchandise
		fields = ['price_category','created']


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
		fields = ['jewel_type','price_category','created',]


class AccessoryFilter(MerchandiseFilterBase):
	jewel_type = django_filters.MultipleChoiceFilter(
		choices = Jewel.JEWEL_TYPE,
		widget=forms.CheckboxSelectMultiple(),
	)
	metal_type = django_filters.MultipleChoiceFilter(
		choices = Accessory.METAL_TYPE,
		widget=forms.CheckboxSelectMultiple(),
	)
	class Meta:
		model = Accessory
		fields = ['jewel_type','metal_type','price_category','created']

class PearlFilter(MerchandiseFilterBase):
	pearl_type = django_filters.MultipleChoiceFilter(
		choices = Pearl.PEARL_TYPE,
		widget=forms.CheckboxSelectMultiple(),
	)
	min_size = django_filters.NumberFilter(lookup_expr='gt')
	max_size = django_filters.NumberFilter(lookup_expr='lt')
	class Meta:
		model = Pearl
		fields = ['pearl_type','price_category','min_size','max_size','created']

class DiamondFilter(MerchandiseFilterBase):
	#carat = django_filters.NumberRangeFilter()
	class Meta:
		model = Diamond
		fields = ['color','clarity','cut','created']


class ColoredGemFilter(MerchandiseFilterBase):
	class Meta:
		model = ColoredGem
		fields = ['created']

