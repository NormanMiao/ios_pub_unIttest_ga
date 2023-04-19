import logging
import sys
import time
import os
from gautomator.by import By
from gautomator.gautomator import GAutomator
import unittest
host = "127.0.0.1"
port = int(os.environ.get("GA_SDK_PORT"))

class TestGaDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化"""
        pass
    
    @classmethod
    def tearDownClass(cls):
        """结束"""
        pass


    def test_action_rpg(self):
        os.system("pkill -f 'goios launch com.epicgames.ActionRPG'")
        time.sleep(3)
        os.system("goios --udid $UDT_DEVICE_SERIAL launch com.epicgames.ActionRPG")
        time.sleep(10)
        ga = GAutomator(host="127.0.0.1", port=port)
        ga.find_game_element(By.TEXT, "OPTIONS").click()
        ga.context = ga.UE_SLATE
        time.sleep(2)
        ga.find_game_element(By.WIDGET_PATH, ".../HorizontalBox_64/SFX_Checkbox/SCheckBox.cpp(482)/SCheckBox.cpp("
                                         "497)/TextBlock_1").click()
        time.sleep(3)
        ga.find_game_element(By.WIDGET_PATH, ".../HorizontalBox_64/SFX_Checkbox/SCheckBox.cpp(482)/SCheckBox.cpp("
                                         "497)/TextBlock_1").click()
        time.sleep(1)
        ga.find_game_element(By.TEXT, "BACK").click()
        time.sleep(3)
        ga.context = ga.UE_UMG
        ga.find_game_element(By.TEXT, "START GAME").click()
        time.sleep(1)
        ga.find_game_element(By.NAME, "SkipLabel").click()
        time.sleep(1)
        # AUTO PLAY
        ga.find_game_element(By.NAME, "TextBlock_0").click()
        time.sleep(120)
        res = ga.find_game_elements(By.NAME, "TextGameOver")
        assert len(res) > 0
   


