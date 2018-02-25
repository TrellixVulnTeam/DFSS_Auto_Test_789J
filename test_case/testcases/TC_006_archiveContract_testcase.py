# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.ArchiveContractPage import ArchiveContractPage
from data.TestData import Data
import time


class ArchiveContractTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统-管理端
    def user_login_verify(self, username="sunquan", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)


    # 合同归档--以公司名义签订
    def test_1_archiveContractForCMP(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.archiveContractForCMP()
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__archiveContractForCMP.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()

    # 合同归档--以个人名义签订
    def aa_test_2_archiveContractForPerson(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.archiveContractForPerson()
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__archiveContractForPerson.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()

    #合同打回
    def aa_test_3_rejectContract(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.rejectContract(Data.ctr_reject_memo)
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__rejectContract.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()
    #合同作废
    def AA_test_4_discarContract(self):
        self.user_login_verify()
        arc_contract = ArchiveContractPage(self.driver)
        arc_contract.gotoNeedAchiveList(Data.cmp_name)
        arc_contract.discarContract(Data.ctr_discar_memo)
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__discarContract.png")
        arc_contract.setWaitTime(2)
        arc_contract.close()

if __name__ == '__main__':
    unittest.main()


