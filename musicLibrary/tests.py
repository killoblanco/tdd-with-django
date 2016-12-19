from django.test import LiveServerTestCase
from selenium import webdriver

from solos.models import Solo


class StudentTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.browser.implicitly_wait(2)
        self.solo1 = Solo.objects.create(
            instrument="saxophone",
            artist="John Coltrane",
            track="My Favorite Things",
            album='My Favorite Things'
        )
        self.solo2 = Solo.objects.create(
            instrument="saxophone",
            artist="Cannonball Adderley",
            track="All Blues",
            album='Kind of Blue',
            start_time='2:06',
            end_time='4:01'
        )
        self.solo3 = Solo.objects.create(
            instrument="saxophone",
            artist="Cannonball Adderley",
            track="Waltz for Debby",
            album='Know What I Mean?'
        )

    def find_search_results(self):
        return self.browser.find_elements_by_css_selector('.jmad-search-result a')

    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """
        # Steve is a jazz student who would like to find more
        # examples of solos so he can improve his own
        # improvisation. He visits the home page of JMAD.
        home_page = self.browser.get(self.live_server_url + '/')
        # He knows he's in the right place because he can see
        # the name of the site in the heading.
        brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        # He sees the inputs of the search form, including
        # labels and placeholders.
        instrument_input = self.browser.find_element_by_css_selector('input#jmad-instrument')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-instrument"]'))
        self.assertEqual(instrument_input.get_attribute('placeholder'), 'i.e. trumpet')
        artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element_by_css_selector('label[for="jmad-artist"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Davis')
        # He types in the name of his instrument and submits it.
        instrument_input.send_keys('saxophone')
        instrument_input.submit()
        # He sees too many search results...
        search_result = self.find_search_results()
        self.assertGreater(len(search_result), 2)
        # ...so he adds an artist to his search query and
        second_artist_input = self.browser.find_element_by_css_selector('input#jmad-artist')
        second_artist_input.send_keys('Cannonball Adderley')
        second_artist_input.submit()
        second_search_result = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertEqual(len(second_search_result), 2)
        # gets a more manageable list.
        second_search_result = self.find_search_results()
        self.assertEqual(len(second_search_result), 2)
        # He clicks on a search result.
        second_search_result[0].click()
        # The solo page has the title, artist and album for
        # this particular solo.
        # import pdb
        # pdb.set_trace()
        self.assertEqual(self.browser.current_url, '{}/solos/2/'.format(self.live_server_url))
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-artist').text, 'Cannonball Adderley')
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-album').text, 'Kind of Blue')
        # He also sees the start time and end time of the solo.
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-start-time').text, '2:06')
        self.assertEqual(self.browser.find_element_by_css_selector('#jmad-end-time').text, '4:01')
        # self.fail('Incomplete Test')

    def tearDown(self):
        self.browser.quit()
