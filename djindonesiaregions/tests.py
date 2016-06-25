from django.test import TestCase

from djindonesiaregions.djindonesiaregions.models import Province, District, Regency, Village


class IndonesiaRegionsTestCase(TestCase):

    def test_data_loaded(self):
        self.assertTrue(Province.objects.all().exists())
        self.assertTrue(Regency.objects.all().exists())
        self.assertTrue(District.objects.all().exists())
        self.assertTrue(Village.objects.all().exists())

    def test_getting_individual_data(self):
        province = Province.objects.get(province_id='61')
        self.assertEqual(province.name, 'KALIMANTAN BARAT')
        regency = Regency.objects.get(regency_id='1611')
        self.assertEqual(regency.name, 'KABUPATEN EMPAT LAWANG')
        district = District.objects.get(district_id='3508080')
        self.assertEqual(district.name, 'KUNIR')
        village = Village.objects.get(village_id='1103041012')
        self.assertEqual(village.name, 'SILOLO')

