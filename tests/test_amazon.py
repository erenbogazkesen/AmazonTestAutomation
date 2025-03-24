import unittest
 

from selenium import webdriver

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultPage


class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #kullanacağımız nesnelerin oluşturulması
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def tearDown(self):

        self.driver.quit()

    def test_amazon(self):
        search_keyword = "samsung"
        product_index = 3
        page_number=2


        # 1.Ana sayfaya git
        self.home_page.go_to_url("https://www.amazon.com.tr/")

        # 2.Sayfanın açıldığını doğrula
        self.assertTrue(self.home_page.is_on_home_page(),"This page is not homepage")

        # 3.Arama kutusuna samsung yaz ve ara
        self.home_page.search_product(search_keyword)

        # 4.Arama sonuçlarından sonra listelenen ürünlerin Samsung ürünler olduğunu doğrula
        self.assertGreater(len(self.search_results_page.check_samsung_products()), 0, "No Samsung products found!")

        #5.İkinci sayfa numarasına tıklamak için sayfayı aşağı kaydırıyoruz
        self.search_results_page.scroll_page()

        #6.sayfanın altındaki sayfalar arası geçiş elementinin görünürlüğünü doğrulama
        self.assertTrue(self.search_results_page.check_number_bar_visible(),"The number bar cannot be displayed.")

        #7. 2.sayfaya gitmemizi sağlayacak fonksiyon
        self.search_results_page.click_page_number()

        #8. URL ile gittiğimiz sayfanın gitmek istediğimiz sayfa olup olmadığını doğrulayan fonksiyon
        self.assertIn(f"sr_pg_{page_number}", self.search_results_page.get_current_url(), "2nd page is not displayed!")

        #9. 3.sıradaki ürüne tıklamak için sayfayı aşağı kaydırıyoruz
        self.driver.execute_script("window.scrollTo(0, 500);")

        # Ürünü seçmek için sayfadaki fotoğrafları kullandım fakat doğru seçim için magic number (+4) kullanmak zorunda kaldım
        self.search_results_page.click_product(product_index+4)

        #10. Ürüne tıkladıktan sonra ürün sayfasında olup olmadığımızı doğrulayan fonksiyon
        self.assertTrue(self.product_page.is_on_product_page(),"This page is not on product page")
        product_name = self.product_page.get_product_title()

        #11. Ürün sayfası doğrulandıktan sonra ürünü sepete ekleme işlemi
        self.product_page.add_to_cart()

        #12. Ürün sepete eklendikten sonra "sepete eklendi" ifadesi yardımıyla ürünün eklenip eklenmediğinin kontrolü
        self.assertTrue(self.product_page.is_product_added_to_cart(),"Product is not added to cart")

        #13. Sepete eklenme kontrolü yapıldıktan sonra sepete gitme
        self.cart_page.go_to_cart_page()
        #sepetteki ürünün ismini alıyoruz karşılaştırma yapıp doğru ürünü ekleyip eklemediğimizi kontrol etmek için
        cart_name=self.cart_page.get_product_title()

        #14. Eklediğimiz ürün ile sepetteki ürünün aynı olup olmadığını kontrol etmek için isim karşılaştırması
        self.assertEqual(product_name,cart_name, "The product you added and the product in the basket are different")

        #15. Sepetteki ürünü silme
        self.cart_page.delete_product()

        #16. Sepetin boş olduğunun doğrulama işlemi
        self.assertEqual(self.cart_page.empty_cart_message_is_displayed(),"Ara toplam (0 ürün):","Cart is not empty")

        self.cart_page.go_to_home_page()

        # 17.Ana sayfanın tekrar açıldığını doğrula
        self.assertTrue(self.home_page.is_on_home_page(), "This page is not homepage")


if __name__ == '__main__':
    unittest.main()